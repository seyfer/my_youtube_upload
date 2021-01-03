This is a set of scripts I used to upload 300GB of videos to YouTube from Ubuntu.

It depends on a python package, you have to install it.

```
$ wget https://github.com/tokland/youtube-upload/archive/master.zip
$ unzip master.zip
$ cd youtube-upload-master
$ sudo python setup.py install
```

Then do the following:

* Get client_secrets.json from Google API for YouTube. 
* Save this file in the same directory with these scripts.
* Edit my_upload.py to change playlist and other parameters.
* Edit *.sh scripts with your path to videos folder.
- Or better do a PR, to convert hardcoded path into console parameters. :)
