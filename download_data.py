import tarfile
import zipfile
import sys
import os
import urllib.request

def show_progress(i, total, size):
	'''Shows download progress for the BabI dataset'''
	remaining = float(i * total) / size
	progress = '\r- Sucessfully downloaded : {0:.1%}'.format(remaining)
	sys.stdout.write(progress)
	sys.stdout.flush()

def download(url, directory):
	'''Downloads and extracts the file(zipfile or tarfile)
	:param url
	:param directory
	'''
    filename = url.split('/')[-1]
    file_path = os.path.join(directory, filename)
    
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    
    if not os.path.exists(file_path):
        if not os.path.exists(directory):
            os.makedirs(directory)
    
        file_path, _ = urllib.request.urlretrieve(url=url, filename=file_path, reporthook=show_progress)

        if file_path.endswith(".zip"):
            zipfile.ZipFile(file=file_path, mode="r").extractall(directory)
        elif file_path.endswith((".tar.gz", ".tgz")):
            tarfile.open(name=file_path, mode="r:gz").extractall(directory)
        print("Download Complete.")
    else:
        print("Dataset already downloaded or present.")

def main():
	babi_dataset = 'http://www.thespermwhale.com/jaseweston/babi/tasks_1-20_v1-2.tar.gz'
	glove_vector = 'http://nlp.stanford.edu/data/wordvecs/glove.6B.zip'
	directory = 'data/'
	download(babi_dataset , directory)
	download(glove_vector, directory)

if __name__ == '__main__':
	main()