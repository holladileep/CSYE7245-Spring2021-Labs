import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Imports the modules
import requests
from bs4 import BeautifulSoup
import os
import shutil

# Root URL

root_URL = 'http://www.dermnet.com/'


def find_max(link_):
    r_ = requests.get(link_)
    html_page1_1 = r_.text
    soup_page1_1 = BeautifulSoup(html_page1_1, "html.parser")

    navigationL = soup_page1_1.find_all("div", attrs={"class": "pagination"})
    max_ = 1
    last_ = 1

    if not navigationL:
        pass
    else:
        for navi_ in navigationL:
            for i in navi_.children:
                try:
                    i_ = i.contents[0]
                except:
                    pass
                else:
                    if i_ == 'Next':
                        max_ = int(last_)
                        break
                    else:
                        last_ = i_
    return int(max_)


# Function to convert images to downloadble link for the images

def images2links(imagesL):
    thumbRLinks = []

    for url_ in imagesL:

        soup_page1_1_ = BeautifulSoup(requests.get(url_).text, "html.parser")

        for link in soup_page1_1_.find_all("img"):
            link_ = link.get("src")
            if 'Thumb' in link_:
                thumbRLinks.append(link_.replace('Thumb', ''))
    return list(set(thumbRLinks))


def download(url, image_path):
    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(image_path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except Exception as e:
        print(e)
        print("Failed to save " + image_path)
        print(url + "\n")

    else:
        print("Successfully saved " + image_path)


def upload_models():
    import boto3
    from datetime import datetime
    import os
    # Connect to Boto3
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-2')

    # Replace this with your S3 Bucket
    bucket_name = 'holladileep'

    model_files = [os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'retrained_graph_v2.pb')),
                   os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'retrained_labels.txt'))]
    for file in model_files:
        print(file)
        s3.Bucket(bucket_name).upload_file(Filename=file,
                                           Key='model/' + datetime.today().strftime(
                                               '%Y-%m-%d-%H:%M:%S') + '_' + os.path.basename(file))
        print('Upload Complete')


def get_data():
    type_name = ['Acne-and-Rosacea-Photos']

    type_LinksA = []
    type_PagesA = []
    type_SubLinksA = []

    for sub_ in type_name:
        SubLinks = []
        r_ = requests.get(root_URL + '/images/' + sub_)
        html_page1 = r_.text
        soup_page1 = BeautifulSoup(html_page1, "html.parser")

        for link in soup_page1.find_all('a'):
            id_ = link.get('href')
            if '/images/' in id_:
                SubLinks.append(root_URL + id_)
        type_LinksA.append(SubLinks)

    attr = '/photos/'

    for type_ in type_LinksA:
        maxL_ = []
        thumbRLinks = []

        for link_ in type_:
            imagesL = []
            max_ = find_max(link_)
            maxL_.append(max_)
            print(link_)
            for i_ in range(max_):
                imagesL.append(link_ + attr + str(i_ + 1))

            print("Pages: ", len(imagesL))
            realLinks = images2links(imagesL)
            print("Links: ", len(realLinks))
            thumbRLinks.append(realLinks)

        type_PagesA.append(maxL_)
        type_SubLinksA.append(thumbRLinks)

    # Store the scraped data in /ScrapedData dir
    dir_root_stored_images = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ScrapedData-'))

    if os.path.exists(dir_root_stored_images):
        pass
    else:
        os.mkdir(dir_root_stored_images)
    for category in type_name:
        iloc = type_name.index(category)
        dir_disease = dir_root_stored_images + category + '/'

        if os.path.exists(dir_disease):
            pass
        else:
            os.mkdir(dir_disease)

        print("Disease: ", dir_disease)
        for sub_ in type_LinksA[iloc]:
            iloc_sub = type_LinksA[iloc].index(sub_)

            dir_sub_disease = dir_disease + sub_.split('/')[-1]

            if os.path.exists(dir_sub_disease):
                pass
            else:
                os.mkdir(dir_sub_disease)

            for l_ in type_SubLinksA[iloc][iloc_sub]:
                img_path = dir_sub_disease + '/' + l_.split('/')[-1]
                img_url = l_
                download(img_url, img_path)


def clean_data():
    import os
    import shutil
    folders = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ScrapedData-Acne-and-Rosacea-Photos'))

    for folder in list(os.walk(folders)):
        if not os.listdir(folder[0]):
            os.removedirs(folder[0])

    for folder in list(os.walk(folders)):
        if len(os.listdir(folder[0])) < 15:
            print(folder[0] + ' removed')
            shutil.rmtree(folder[0])


def model_training():
    from subprocess import call
    call(["python", os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'train.py'))])


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'concurrency': 1,
    'retries': 0,
    'depends_on_past': False,
}

with DAG('CNN-Training-Pipeline',
         catchup=False,
         default_args=default_args,
         schedule_interval='@once',
         ) as dag:
    t0_start = PythonOperator(task_id='UploadModels',
                              python_callable=upload_models)
    t1_getdata = PythonOperator(task_id='ScrapeData',
                                python_callable=get_data)
    t2_cleanup = PythonOperator(task_id='Cleanup',
                                python_callable=clean_data)
    t3_train = PythonOperator(task_id='TrainModel',
                              python_callable=model_training)
    t4_upload = PythonOperator(task_id='UploadModelsPostTraining',
                               python_callable=upload_models)

t0_start >> t1_getdata >> t2_cleanup >> t3_train >> t4_upload