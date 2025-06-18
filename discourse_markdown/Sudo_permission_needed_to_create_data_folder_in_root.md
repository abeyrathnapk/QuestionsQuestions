# Sudo permission needed to create data folder in root?

[View on Discourse](https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072)

---
**vikramjncasr** on 2025-02-14T03:57:16.864Z:

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir please help

When I am downloading the data folder after processing datagen.py , it is
trying to download in root folder and it is facing permission error . how can
we overcome this ?  
needs sudo permission all the time…  

[![Here's alt text describing the image: A screenshot of a terminal window
displaying the output of a Linux `ls /` command. The background is dark,
almost black. The text is primarily displayed in shades of blue and green,
with some light gray for certain characters. The top line shows a command
prompt: `vikramjncasr@ANJANEYA:/mnt/c/IIT_Madras/TDS_Project_1$ ls /`. Below,
the command lists the contents of the root directory, including folders such
as `bin`, `boot`, `etc`, `home`, `lib`, `media`, `proc`, `root`, and `usr`,
among many others. The `tmp` folder is highlighted in a light green color. The
bottom line shows a new command prompt showing the user remains in the same
directory.](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae_2_690x70.png)image2100×216
100 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae.png
"image")



---
**carlton** on 2025-02-14T04:53:36.939Z:

Hi Vikram,

This is because (if you watched the session, or examined the code, you would
have realised that) datagen.py was designed to run inside your docker
container. And datagen.py (or a similar named file which we will not tell you
ahead of time and will be provided as the query parameter in task A1) will
normally be called by evaluate.py  
Inside the docker container, permission for the data folder is set by the
Dockerfile  
which then allows your application to access the root folder inside your
docker image and create the /data folder.

So the workflow is like this (for your internal testing only… please follow
the Project page for deliverables and evaluation to submit project
successfully):

  1. You create your application server that serves 2 endpoints on localhost:8000
  2. You create a docker image that runs this application server.
  3. You run the docker image using podman as described in the project page.
  4. For mimicking the testing conditions. You need two files:  
evaluate.py and datagen.py to be in the same folder where you are running
these two scripts.

  5. Run evalute.py using uv.

If your docker image is correctly configured and your application is correctly
configured, then all the tasks run by evaluate.py will correctly tell you if
the application is producing the right result for each task.

Hope that gives clarity.

Kind regards



