# Tds-official-Project1-discrepencies

[View on Discourse](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141)

---
**Jivraj** on 2025-03-28T18:34:41.099Z:

Please post any discrepancies related to project1.

[@carlton](/u/carlton)

## Who were evaluated? How did we decide what to evaluate?

All the image ids we evaluated were what _you_ submitted to us. This is the
list of docker repos that was given to us by [@s.anand](/u/s.anand) as the
official list that met all the pre-requisites of Project 1. Therefore we will
only evaluate those on this list who are eligible for evaluation with the
repos _you_ gave us.

For clarity. Your docker repo gets a unique id every time it is changed. We
will ONLY evaluate the image id which was present at the time of the docker
repo being pulled. This acts as a time stamped frozen version of your repo. No
other image id will be evaluated.

## How to fix bugs in our scripts

Create Pull requests to [Jivraj-18/tds-
jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1) .

### **Docker Image Architecture Issue Report**

If your Docker image was run on the wrong architecture, please fill out this
form:  
[Submit
Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

## Bug fixes

If you find bugs in our evaluation scripts, you might benefit from more marks
because of the bug fix. So it is in your interest to look through our scripts
and logs and identify bugs or anomalies. You might just go from 0 to heros.

Kind regards,  
TDS Team



---
**Jivraj** on 2025-03-28T18:35:12.862Z:





---
**23f2004912** on 2025-03-28T19:03:42.095Z:

What is the highest mark anyone has scored? Is it 22/20  
[@Carlton](/u/carlton)?



---
**23f2005702** on 2025-03-28T19:11:04.307Z:

How come me and my group used same code but some got 10 some 11 some 12?



---
**Yogesh1** on 2025-03-28T19:11:39.267Z:

[@carlton](/u/carlton) Please make clear what the average marks are, what
highest marks are, and how the project will be evaulated.

We are very close to the end semester exam, and we are still not clear on
assignment and project marks. It is a bit frustrating to plan in such
circumstances.



---
**carlton** on 2025-03-28T19:12:51.933Z:

You have to see the logs for that. We have shared the logs. Everyone was
graded by the exact same code, so there is no partiality. Your code did not
produce consistent results.



---
**22f3002933** on 2025-03-28T19:14:57.376Z:

I have noticed that my image was run on a `x86_64` architecture ( I can see my
email in the logs shared ) whereas I built this docker image on my mac which
is `ARM`. This is why I can see that my docker image never ran properly and
threw the `exec format error`.

This was never mentioned on which architecture machine, our images will be
evaluated. I request that my evaluation be done again on the right machine.



---
**22f2001389** on 2025-03-28T19:15:19.619Z:

My evaluation log file is missing, although I followed all the steps to
generate the docker image correctly, it’s showing the server didn’t start for
5 minutes but when I uploaded it, it was working fine. Please help me out sir,
I worked hard on the project. I’ll get a zero, but I made the submissions
correctly. Some other student also got the “server didn’t start in 5 minutes”
but he has an evaluation log file. Please kindly help me out. My roll no. is
22f2001389



---
**carlton** on 2025-03-28T19:16:38.027Z:

We will check and rerun on arm if we ran it on the wrong emulation.



---
**22f2001389** on 2025-03-28T19:19:15.240Z:

Any suggestions for my case sir ? I’m really tensed.



---
**21f2000709** on 2025-03-28T19:20:38.723Z:

![[Image description unavailable]](https://dub1.discourse-
cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002933/48/118648_2.png)
22f3002933:

> I have noticed that my image was run on a `x86_64` architecture ( I can see
> my email in the logs shared ) whereas I built this docker image on my mac
> which is `ARM`. This is why I can see that my docker image never ran
> properly and threw the `exec format error`.
>
> This was never mentioned on which architecture machine, our images will be
> evaluated. I request that my evaluation be done again on the right machine.

[@carlton](/u/carlton) same issue, My image was also run on a `x86_64`
architecture. I too built on my mac which is `ARM` (M1 Processor). I too can
see that my docker image never ran properly and threw the `exec format error`
and **Evaluation log file** is MISSING.

Actually my image was run on x86_64 architecture as it was present in that log
file and because of the wrong architecture it never started.

I also request that my evaluation be done again on the right machine.

[![[Image description unavailable]](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_690x77.png)Screenshot
2025-03-29 at 12.51.59 AM1613×182 19.1 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d.png
"Screenshot 2025-03-29 at 12.51.59 AM")

Even just now I tried running the exact image:  

[![[Image description unavailable]](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2_2_690x95.png)Screenshot
2025-03-29 at 12.53.35 AM1220×169 25.8 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2.png
"Screenshot 2025-03-29 at 12.53.35 AM")

It is running fine on my macbook air m1 (ARM)

[@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)



---
**23f1002056** on 2025-03-28T19:26:23.746Z:

![[Image description unavailable]](https://dub1.discourse-
cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f2001389/48/12849_2.png)
22f2001389:

> uploaded

Facing the same issue sir, kindly look into it. I had made sure all the files
including the docker file were working perfectly fine. Please help me out.  
Roll no. 23f1002056



---
**22f1000703** on 2025-03-28T19:27:25.982Z:

My evaluation log file is missing in report provided. It says tasksA was not
found. but I have submitted tasksA in my project file. Also it says server
didnt start for 5 mins but for me image was working fine. please kindly help
me out. I have made submissions correctly. I request for re evaluation of my
project. my roll no is 22f1000703



---
**22f3003083** on 2025-03-28T19:30:09.940Z:

Respected,

I haven’t received any mail yet regarding the TDS Project 1 marks.  
Please look into it.

Regards,  
Soham



---
**AYUSH_SINGH** on 2025-03-28T19:37:05.650Z:

My evaluation log file is missing.  
The 2 other log files i’m given doesnt have my email inside it listed.  
the Image id which is given in the MAIL is not present in my docker desktop,
my project’s docker image is listed in docker desktop, which doesnot matches
the image id given in the MAIL,  
What was evaluated? How it was evaluated?

This is the id of the docker image that was evaluated: 0ade87d1bf07

My terminal shows 2 images as last, with respective image ids. I am not sure
which one is the real, so please check with both the ids.  
tds-project-1 latest c854274f078d 5 weeks ago 1.38GB  
ayush6871/fastapi-agent latest 27e8375b0ab1 6 weeks ago 1.66GB

I am requesting to look into this case. I think there has been some mistake
somewhere.

21f3001194



---
**Adithya** on 2025-03-28T19:42:12.154Z:

I have also built the image on Mac and facing the same issue

`exec format error`

It is running fine on my Macbook Pro M1

[@carlton](/u/carlton) [@Saransh_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)



---
**22f2001389** on 2025-03-28T19:44:32.573Z:

Sir I have noticed a technical glitch for the docker issue, wherein I
mistakenly uploaded the wrong docker image link so kindly please kindly re
evaluate it.



---
**Abhay222** on 2025-03-28T19:53:44.965Z:

Sir I haven’t received any mail regarding this Project1 marks.
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)



---
**21f3000512** on 2025-03-28T19:54:41.344Z:

[@carlton](/u/carlton) Sir , my Docker image is built on Macbook M1 which as
you know uses ARM64 architecture . But evaluated with x86_64 which caused the
exec format error due to cross platform compatibility issues . I am kindly
requesting you to re-evaluate the project once again .



---
**HarshJaiswal** on 2025-03-28T20:04:57.116Z:

This is the id of the docker image that was evaluated: d0f14a872042 , but i
had never provided this docker image then how it get evaluated, also none of
the docker image created by me has this id.

Please, look over it.

Regards,  
Harsh Jaiswal  
23f1001995



