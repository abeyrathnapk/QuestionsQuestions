# GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]

[View on Discourse](https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247)

---
**s.anand** on 2025-01-14T13:00:03.324Z:

Please post any questions related to [Graded Assignment 3 - Large Language
Models](https://exam.sanand.workers.dev/tds-2025-01-ga3).

* * *

## Important Instruction

Please use markdown code formatting (fenced code blocks) when sharing code in
Discourse posts. This makes the code much easier to read and differentiate
from non-code text. It also makes it easier for people to copy code snippets
and run it themselves. See below code for example

    
    
    ping exam.sanand.workers.dev
    
    Pinging exam.sanand.workers.dev [104.21.31.149] with 32 bytes of data:
    Reply from 104.21.31.149: bytes=32 time=9ms TTL=58
    Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
    Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
    Reply from 104.21.31.149: bytes=32 time=9ms TTL=58
    
    Ping statistics for 104.21.31.149:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 8ms, Maximum = 9ms, Average = 8ms
    

Visit this link for more details: [Extended Syntax | Markdown Guide](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

A friendly suggestion: kindly go through [Discourse Docs](/c/docs-
discourse/45)! ![Here's alt text for the image: "A simple, smiling emoticon.
The emoticon is a bright yellow circle with two small, dark brown or black
dots for eyes and a small, upward-curving black line for a mouth. The overall
expression is one of gentle happiness."](https://emoji.discourse-
cdn.com/google/slight_smile.png?v=12)

* * *

Deadline: Sunday, February 2, 2025 6:29 PM

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)



---
**s.anand** on 2025-01-14T13:06:47.583Z:





---
**nilaychugh** on 2025-01-15T12:20:05.475Z:

how to get the dummy API key?



---
**Jivraj** on 2025-01-15T14:59:06.607Z:

Hi Nilay,

In order to make a api call to openai chat completions you are required to
send authentication information(openai key) in headers. For first question of
GA3 you don’t have to send actual(working) api key, any dummy api key would
work(you can put your name, or tds anything works)

kind regards



---
**nilaychugh** on 2025-01-18T04:43:01.431Z:

which API should i use in 7th question



---
**22f3001315** on 2025-01-19T07:36:55.428Z:

need help in question 4th. how can i correct this json body? sir
[@Jivraj](/u/jivraj)

    
    
    {
      "model": "gpt-4o-mini",
      "messages": [
        {
          "role": "user",
          "content": "Extract text from this image."
        },
        {
          "role": "user",
          "content": {
            "image_url": "data:image/png;base64,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"
          }
        }
      ]
    }
    
    

error:The JSON body must have 1 message

    
    
    {
      "model": "gpt-4o-mini",
      "messages": [
        {
          "role": "user",
          "content": {
            "text": "Extract text from this image.",
            "image_url": "data:image/png;base64,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"
          }
        }
      ]
    }
    
    

Error: The message must have a 2 content parts



---
**22f3001315** on 2025-01-19T16:53:34.970Z:

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir plz see it once.



---
**Jivraj** on 2025-01-21T07:02:52.278Z:

Hi [@22f3001315](/u/22f3001315) ,

You are almost correct, there are very minor changes that needs to be made.

Take help from Chat GPT or use this documentation which have correct json body
[Vision - OpenAI API](https://platform.openai.com/docs/guides/vision).

Kind regards  
Jivraj



---
**22f3001315** on 2025-01-21T08:21:45.804Z:

it worked thanks sir



---
**22f3002034** on 2025-01-21T11:25:57.882Z:

Are we supposed to buy open ai api key ?



---
**23f2000237** on 2025-01-21T12:01:17.870Z:

No, if you scroll down to the last question, we can get our Ai Proxy key



---
**carlton** on 2025-01-21T12:06:09.235Z:

[@nilaychugh](/u/nilaychugh) [@22f3002034](/u/22f3002034)

The API key is available at <https://aiproxy.sanand.workers.dev/>

The instructions on how to use the token is given at [GitHub -
sanand0/aiproxy: Authorizing proxy for
LLMs](https://github.com/sanand0/aiproxy)

You cannot use this token directly with Open AI or any other gpt. These are
only valid via the API exposed by the above instructions.

You get a limit of $1. Use with care.

Kind regards



---
**nilaychugh** on 2025-01-21T14:30:30.322Z:

but the embedding model that is said to be used is text embedding 3 small,
which is the model of OpenAI



---
**Jivraj** on 2025-01-22T09:13:43.408Z:

Hi Nilay,

Yes you would need to use `text-embedding-3-small` model of openai for
embedding questions.

Kind regards  
Jivraj



---
**nilaychugh** on 2025-01-23T03:52:39.679Z:

i have a doubt, while submitting the GA3, both 7th and 8th questions require
the API url to be active and connected right, but its not possible as both the
URLs use same port, so if we check my 7th question URL is running right now,
it’ll show as correct, but then if i run 8th question URL, the 7th question
will automatically show the error, **is there any solution to this problem?**



---
**21f3002277** on 2025-01-23T06:09:55.493Z:

Q5. How to handle the error ? sir [@Jivraj](/u/jivraj)

Error: The first input does not match the first text exactly



---
**21f3002277** on 2025-01-23T06:17:12.711Z:

Q4. How to handle this error? [@Jivraj](/u/jivraj)

    
    
    {
      "id": "chatcmpl-AshDCPwSiXNao1QXmCxCmi63GifFx",
      "object": "chat.completion",
      "created": 1737599182,
      "model": "gpt-4o-mini-2024-07-18",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "The image contains an email address and a number. The email address appears to be associated with an educational institution, and the number seems to be a numerical sequence.",
            "refusal": null
          },
          "logprobs": null,
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 592,
        "completion_tokens": 33,
        "total_tokens": 625,
        "prompt_tokens_details": {
          "cached_tokens": 0,
          "audio_tokens": 0
        },
        "completion_tokens_details": {
          "reasoning_tokens": 0,
          "audio_tokens": 0,
          "accepted_prediction_tokens": 0,
          "rejected_prediction_tokens": 0
        }
      },
      "service_tier": "default",
      "system_fingerprint": "fp_bd83329f63",
      "monthlyCost": 0.05490624000000001,
      "cost": 0.001974,
      "monthlyRequests": 14,
      "costError": "crypto.createHash is not a function"
    }
    

Error: Model must be gpt-4o-mini



---
**Jivraj** on 2025-01-23T10:58:14.611Z:

Hi Nilay,

![Here's alt text describing the image: "A stylized four-leaf clover sits
centrally on a pale lavender background. The clover is rendered in shades of
teal and dark teal, with a subtle gradient effect giving the leaves a slightly
three-dimensional look. The background is a light lavender that is bisected by
a diagonal line, creating two differently angled planes of color. There is no
text present."](https://dub1.discourse-
cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/nilaychugh/48/84996_2.png)
nilaychugh:

> both the URLs use same port,

You can run two servers on different port numbers.



---
**Jivraj** on 2025-01-23T11:05:13.578Z:

Hi Vikash,

I looked at your answers in backend. In answer you submitted response from
openai, but you need to submit json object which is required for sending a
request to LLM.

Kind regards



---
**Jivraj** on 2025-01-23T11:07:22.861Z:

You made same mistake here, instead of response use json body that’s required
for sending request to LLM.

Kind regards



