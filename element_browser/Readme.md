# Element Browser

## Overview

#### Element Browser play a significant role in the daily VFX workflow. It is very important that these Browser are well structured and organized so artists can quickly find the element that best fits for the shot.

This will support Multiple DCC's like Nuke, Maya and Blender.

Artist can able to publish the file and read the files via the element browser.

Following is the features for the browser,
1. Cross-platform support
2. Every user can able customize their element by click on the Favorite's.
3. User can filter based on the element name, keyword, file format, frames, file catogery, etc.
4. Mouse hover scroll to play the images or qt.
5. Setting to change the storage location and other options.
6. Proxy/Thumbnail generation

## Installation

It will support for python 2 and 3.

`pip install -r python2_requirements.txt`


FFMPEG flimstrip generation command:

`ffmpeg -loglevel panic -y -i "hcw_f0015.mov" -frames 1 -q:v 1 -vf "select=not(mod(n\,15)),scale=-1:120,tile=20x1" video_preview.jpg`


ORM Model:

`Element` table will contains the element information which include the combination

#### Table: element

| Columns       | Data Type                                      | Description                                        |
|---------------|------------------------------------------------|----------------------------------------------------|
| id            | int AI PK                                      | unique ID and Auto Increment                       |
| ele_parent_id | int                                            | foreign of the element_parent_tagging table        |
| ele_name      | varchar(45)                                    | element name(e.g. low smoke, medium smoke, etc)    |
| ele_type      | enum('ImageSeq','Image','Movie','DCC','Other') | group of file formats contains element type        |
| format        | varchar(45)                                    | extension of the file                              |
| frames        | varchar(45)                                    | no of frames in the sequence or qt or single image |
| comment       | blob                                           | Description about the given element                |
| file_size     | int                                            | size in bytes                                      |
| ele_filepath  | varchar(300)                                   | full file location                                 |
| ele_status    | enum('Active','InActive')                      | file is exists in the storage or not               |

#### Table: element_parent_tagging

| Columns         | Data Type   | Description                                 |
|-----------------|-------------|---------------------------------------------|
| id              | int AI PK   | unique ID and Auto Increment                |
| ele_parent_name | varchar(45) | foreign of the element_parent_tagging table |