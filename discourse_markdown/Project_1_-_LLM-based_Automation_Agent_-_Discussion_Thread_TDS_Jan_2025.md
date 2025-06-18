# Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]

[View on Discourse](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277)

---
**s.anand** on 2025-01-19T08:17:46.856Z:

Please post any questions related to [Project 1 - LLM-based Automation
Agent](https://tds.s-anand.net/#/project-1).

Deadline: Sunday, February 16, 2025 6:29 PM

**Update on 27 Jan 2025** :

A _sample_ evaluation script for Project 1 tasks A1-A10 is available at
[tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip ·
sanand0/tools-in-data-science-public ·
GitHub](https://github.com/sanand0/tools-in-data-science-
public/tree/tds-2025-01-project-1-wip/project-1)

You can use this to validate your code for Project 1.

Please note:

  1. This is a sample. It **WILL** change.
  2. Don’t rely on the dataset being the same. It **WILL** change.
  3. LLMs give different results each time they are called. Make sure: 
     * Your code gives correct results _reliably_ (i.e. try a few times)
     * Change the task in the evaluation script slightly to test variations
  4. Your [AI Proxy usage](https://aiproxy.sanand.workers.dev/) resets on 1 Feb. You have a limited budget. Utilize what you can this month.
  5. For those who [submit their code](https://docs.google.com/forms/d/e/1FAIpQLSdOaljgV-INdbKrPotV9OMUKV01QVaFEfcnr5dAxBZqM4x37g/viewform?usp=dialog) by Friday 31 Jan, I will run a sample evaluation and share the results.



---
**s.anand** on 2025-01-19T08:20:32.879Z:





---
**roy2003** on 2025-01-19T13:44:38.945Z:

sir show us all the way to do project



---
**Jivraj** on 2025-01-19T13:45:31.017Z:

Hi Shouvik,

We will have live sessions to guide on how to do project.

Kind regards  
Jivraj



---
**23f2000237** on 2025-01-20T10:44:32.687Z:

Will those session be on youtube too?



---
**carlton** on 2025-01-20T10:48:22.899Z:

Hi Sakthivel,

Yes all sessions are being recorded and are available on youtube within a day.  
[Jan 25 TDS
Playlist](https://www.youtube.com/playlist?list=PL_h5u1jMeBCl1BquBhgunA4t08XAxsA-C)

Kind regards



---
**22f3001315** on 2025-01-23T09:57:29.120Z:

[![[Image description unavailable]](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/2/0/20410aa56e88be04883b6f3feca5010089afe276_2_690x67.png)Screenshot
2025-01-23 1516141281×125 18.1 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/2/0/20410aa56e88be04883b6f3feca5010089afe276.png
"Screenshot 2025-01-23 151614")

  
sir [@Jivraj](/u/jivraj) after editing line 127 in datagen.py i got those
required data files. is it allowed ? also i had to run datagen.py MANUALLY(is
this process also should be automatic)?



---
**Jivraj** on 2025-01-23T11:30:21.008Z:

Hi Guddu ,

I didn’t make any changes to file and it worked for me. Can you mention what
is need of making changes ?

command that I used :  
`uv run datagen.py 22f3002542@ds.study.iitm.ac.in --root ./data`

here --root option defines the folder where you want to store generated data.
by default it would try to create a folder in root directory of operating
system.

Kind regards  
Jivraj



---
**23f2005325** on 2025-01-23T13:05:16.643Z:

getting this issue :

    
    
    openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_issuer'}}
    



---
**Jivraj** on 2025-01-23T13:22:03.304Z:

Hi Aishik,

Pls add context to your query, without that we won’t be able to understand,
where exactly you are facing problem.

![[Image description unavailable]](https://dub1.discourse-
cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2005325/48/68296_2.png)
23f2005325:

>
>     openai.AuthenticationError: Error code: 401 - {'error': {'message':
> 'Your authentication token is not from a valid issuer.', 'type':
> 'invalid_request_error', 'param': None, 'code': 'invalid_issuer'}}
>  

Possible reasons for this issue:

  1. Not using anand sir’s proxy url for sending requests.
  2. Token not being correct.



---
**23f2005325** on 2025-01-25T16:20:57.111Z:

yes I was not setting the base url to the proxy. I have fixed it thank you .



---
**23f2005325** on 2025-01-25T18:12:39.754Z:

While implementing task A5, I am confused about what recent actually means in
the phrase “recent log file”, mentioned under task A5, in the problem
statement. This confusion arises because there are no dates corresponding to
the log files. Should I consider log-0 as the most recent one? or the
log-<largest_number> file? Please clarify.



---
**23f2005325** on 2025-01-26T10:30:43.750Z:

I am getting the following response when I am trying to extract credit card
number from the credit-card.png :

    
    
    {'id': 'chatcmpl-<redacted>', 'object': 'chat.completion', 'created': 1737872397, 'model': 'gpt-4o-mini-2024-07-18', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': "I'm sorry, but I can't assist with that.", 'refusal': None}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 946, 'completion_tokens': 11, 'total_tokens': 957, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'service_tier': 'default', 'system_fingerprint': '<redacted>', 'monthlyCost': 0.07715699999999998, 'cost': 0.0029040000000000003, 'monthlyRequests': 31, 'costError': 'crypto.createHash is not a function'}
    

my code is as below :

    
    
    def extract_credit_card_number():
        import requests
        import base64
        import os
        from dotenv import load_dotenv
        load_dotenv()
    
    
    
        BASE_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ["AIPROXY_TOKEN"]}"
        }
    
        image_path = "../data/credit_card.png"
    
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    
        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",  
                    "content": "You are a helpful assistant that provides detailed and accurate descriptions of images. Focus on describing the objects, colors, textures, the overall scene, and most importantly, the text and numbers in the image. Be concise but thorough."
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are given an image containing a credit card number. Extract the credit card number from the image"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
        }
    
        
        response = requests.post(BASE_URL, headers=headers, json=payload)
    
        
        if response.status_code == 200:
            result = response.json()
            print("RESULT:", result)
            cno = result["choices"][0]["message"]["content"]
            print("CREDIT CARD NUMBER:", cno)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    

please guide [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)



---
**23f1000299** on 2025-01-26T17:16:01.337Z:

do we have to do these tasks in the linux? As in some of the GA1, the linux
answers only accepted. Please tell me that, do we can do it in the desktop or
we have to use linux?  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)



---
**Saransh_Saini** on 2025-01-26T18:10:34.636Z:

The bash commands are usually run in a linux machine, but you can easily run
those commands in VSCode without installing any virtual machines. Download the
WSL extension in VSCode and you will get a WSL terminal to work with.

For more information watch this video
<https://youtu.be/q74CP4fB7cY?si=M_zw8WzpmMCyVQat> or watch TDS Live Sessions.

Regards,  
TDS TA



---
**23f1002382** on 2025-01-27T01:27:41.658Z:

what frameworks can we use? hopefully anything?

or what frameworks can’t we use?  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)



---
**carlton** on 2025-01-27T03:04:44.636Z:

Project 1 deliverables are all that matter. How you accomplish them is not
very relevant. The keys to a successful Project 1 are:  
Deliverables,  
and _an example_ of the Evaluation has been provided.  
If your project runs in accordance with the Evaluation methodology then it is
considered.  

[![[Image description unavailable]](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/4/8/488e23f9ea65d35c5ba806fab09f4b5934ed2ed4_2_500x500.png)Screenshot
2025-01-27 at 8.35.23 am1764×1764 374 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/4/8/488e23f9ea65d35c5ba806fab09f4b5934ed2ed4.png
"Screenshot 2025-01-27 at 8.35.23 am")

Please read the documentation carefully from top to bottom.

So the main question is how do you test if the script will run according to
the evaluation? The whole point is for it to run not just on your system. It
should be deployable anywhere on any machine. Your solution should work
anywhere we test it. Thats why you package it in a docker container. How you
achieve that is up to you. But if we cannot run your docker container
according to the specification we have provided then it has failed this
crucial test.

Kind regards



---
**carlton** on 2025-01-27T03:09:21.493Z:

[@23f1002382](/u/23f1002382)

You can use any library as long as your Project 1 meets the deliverable
requirements and does all the (20+) API tasks.

Kind regards



---
**s.anand** on 2025-01-27T13:32:36.477Z:

A _sample_ evaluation script for Project 1 tasks A1-A10 is available at
[tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip ·
sanand0/tools-in-data-science-public ·
GitHub](https://github.com/sanand0/tools-in-data-science-
public/tree/tds-2025-01-project-1-wip/project-1)

You can use this to validate your code for Project 1.

Please note:

  1. This is a sample. It **WILL** change.
  2. Don’t rely on the dataset being the same. It **WILL** change.
  3. LLMs give different results each time they are called. Make sure: 
     * Your code gives correct results _reliably_ (i.e. try a few times)
     * Change the task in the evaluation script slightly to test variations
  4. Your [AI Proxy usage](https://aiproxy.sanand.workers.dev/) resets on 1 Feb. You have a limited budget. Utilize what you can this month.
  5. For those who [submit their code](https://docs.google.com/forms/d/e/1FAIpQLSdOaljgV-INdbKrPotV9OMUKV01QVaFEfcnr5dAxBZqM4x37g/viewform?usp=dialog) by Friday, I will run a sample evaluation and share the results.

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)
\- please socialize this during the live sessions.



---
**Divya1** on 2025-01-27T14:00:22.634Z:

By clicking the project link ,I am getting the notes…but no project is
available in my project 1



