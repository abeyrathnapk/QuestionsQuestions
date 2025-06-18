# Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image

[View on Discourse](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471)

---
**21f3002647** on 2025-02-17T10:07:56.783Z:

Dear TDS Team,

I have verified my submission, and my repository **does include a Dockerfile**
, and the **Docker image is accessible on DockerHub**. Please find the
attached screenshot as proof. Kindly review my submission again and let me
know if any further action is needed.

Looking forward to your confirmation.

Best regards,  
Arnav Mehta  
(21f3002647)

[![Here's alt text describing the image: A dark-themed file directory listing
shows a series of files and folders. The top line displays three dots (...)
indicating more options. Below this are the following items, each with a file
or folder icon: a folder labeled "LLM_PROJECT1", a folder labeled "_pycache_",
a file labeled "Dockerfile", a file labeled "LICENSE", a file labeled
"app.py", a file labeled "datagen.py", a file labeled "evaluate.py", a file
labeled "requirements.txt", a file labeled "tasksA.py", and a file labeled
"tasksB.py". All text is light-colored, likely white or light gray, against
the dark background. The overall style suggests a code editor or file explorer
interface.](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/6/a/6a4a28aa638840e8d2e4dbf246ca235fd41e5ccb.png)image250×534
3.92 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/6/a/6a4a28aa638840e8d2e4dbf246ca235fd41e5ccb.png
"image")

  

[![Here's alt text describing the image: A dark-themed webpage displays
information about a project titled "arnavmehta2025/llm_project1". A light-
grey, three-dimensional cube icon with two small circles on one face is
positioned to the left. The project title is in white, large font. Below it,
in smaller white text, reads "By arnavmehta2025 · Updated 2 days ago". A
small, light-blue "IMAGE" text is also visible. Beneath this, a star icon
indicates zero ratings, and a download icon shows 16 downloads. The overall
color scheme is dark navy blue or black, with light-grey and light-blue
accents.](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/d/1/d14c53cce65e7ac7f679de75bba301f3ee23f1f0.png)image713×238
11 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/d/1/d14c53cce65e7ac7f679de75bba301f3ee23f1f0.png
"image")



---
**21f3002647** on 2025-02-17T12:30:15.244Z:

[@Saransh_Saini](/u/saransh_saini) sir what should i do?



---
**Saransh_Saini** on 2025-02-17T15:43:39.614Z:

[@carlton](/u/carlton) Kindly have a look into this.



---
**satviksawhney** on 2025-02-18T00:48:03.881Z:

Good Morning Sir,  
Sir even I am facing a similar issue, even though sanity check for docker
image on docker hub was cleared but got a mail saying ‘dockerfile’ not present
in the GitHub repo while it clearly was. Sir please look into it we have given
so many days to complete this project.

Looking forward to your reply.

Thank you  
Satvik Sawhney  
23f2003680



---
**carlton** on 2025-02-18T05:00:31.191Z:

So the reason for the failure is:

You had initially put your Dockerfile inside a directory called TDSP-1-main
instead of being directly in your repo. (On 15th Feb 1:26AM)

Then when our automated script checked if students repos met the requirements
and yours did not we immediately sent out a warning email as a opportunity for
students to make the necessary corrections.

Then once you realised your mistake, on **Feb 17th at 9:11 pm IST** i.e
_yesteday_ , you changed your repo to put the files in the correct locations.

Then you finally posted here on Discourse with the image [quote=“21f3002647,
post:1, topic:167471”]  

[![Here's alt text describing the image: "A dark-themed file directory listing
shows a series of files and folders. The top line shows a folder icon followed
by three dots. Below that is a folder labeled 'LLM_PROJECT1,' followed by a
folder labeled '_pycache_'. The remaining lines list files with their names:
'Dockerfile', 'LICENSE', 'app.py', 'datagen.py', 'evaluate.py',
'requirements.txt', 'tasksA.py', and 'tasksB.py'. All file and folder names
are in light-colored text against the dark
background."](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/6/a/6a4a28aa638840e8d2e4dbf246ca235fd41e5ccb.png)image250×534
3.92 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/6/a/6a4a28aa638840e8d2e4dbf246ca235fd41e5ccb.png
"image")

  
[/quote]

showing that your files are in the correct place.

We do not take into consideration modifications to your repo after the
deadline because then we would have to extend that curtesy to all students.

Kind regards



---
**21f3002647** on 2025-02-18T06:35:49.560Z:

[@carlton](/u/carlton) sir  
Yes, I corrected my repo at 9:11 PM IST, but I had actually written and
submitted my query much earlier at 4 PM. At that time, I wasn’t entirely sure
if this was the actual issue, but it looks like it was.

I understand that the deadline had already passed, and I only saw the email
later. I had two GATE papers on the 15th and an interview on the 16th, so I
was extremely busy and couldn’t check my emails sooner. However, I had raised
my concern well before making the correction, so I’d really appreciate it if
my submission could still be considered ![[Image description
unavailable]](https://emoji.discourse-cdn.com/google/frowning.png?v=12)

Kind regards,  
Arnav Mehta  
21f3002647



---
**satviksawhney** on 2025-02-18T08:28:16.577Z:

Sir, please consider it we have spent a lot of time, in my case just the d in
Dockerfile was small that too on remote repository. On my local repository it
was Dockerfile only I even have a published docker image as verified by you
autated script only. The name of the file on remote repository did not change
even after commit it through my local repo, once I read the mail in morning it
was only then I realised it wasn’t changed on GitHub repo.

Sir I understand the deadline has passed and I am not asking for a
resubmission, I am just asking to consider the already submitted work, just
that. It would be really helpful. I just have one commit on my repo that too
“Rename dockerfile to Dokerfile” . Sir please attest consider what we have
already submitted. I have made no changes as you can verify it too.

Sir it is a humble request to please consider it.

Warm Regards,  
Satvik Sawhney  
23f2003680

[![Here's alt text describing the image: A dark-themed file explorer or
similar interface shows a list of files and folders. The list items are
displayed in a row with a folder or file icon to the left, followed by the
name on the left side and a brief description on the right along with a
timestamp. The color scheme is dark gray and black. The entries, from top to
bottom, include: "Business" (folder) with the description "Reconfigured taskB8
taskB9 taskB10", "Operations" (folder) with "Reconfigured taskA8 taskA9
taskA10", "app" (folder) with "Updated Dockerfile and requirements.txt",
"Dockerfile" (file) with "Rename dockerfile to Dockerfile", "LICENSE" (file)
with "MIT License", and "README.md" (file) with "Project Structure". Each line
also indicates the time of the last modification ("2 days ago", "yesterday",
or "3 days ago"). Small icons appear to the far right of each
line.](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/1/a/1a5f2ea044383efcb5d248ddb487665e9e65957d_2_690x170.png)Screenshot
2025-02-18 at 1.53.10 PM1889×467 54 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/1/a/1a5f2ea044383efcb5d248ddb487665e9e65957d.png
"Screenshot 2025-02-18 at 1.53.10 PM")



