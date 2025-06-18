# GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]

[View on Discourse](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959)

---
**s.anand** on 2025-01-31T16:13:36.640Z:

Please post any questions related to [Graded Assignment 4 - Data
Sourcing](https://exam.sanand.workers.dev/tds-2025-01-ga4).

Please use markdown code formatting (fenced code blocks) when sharing code
(rather than screenshots). It’s easier for us to copy-paste and test.

Deadline: Sunday, February 9, 2025 6:29 PM

[@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) [@carlton](/u/carlton)



---
**s.anand** on 2025-01-31T16:14:00.363Z:





---
**22f3001315** on 2025-02-01T07:54:31.100Z:

[![Here's alt text describing the image: "A dark-themed screenshot shows a
code example demonstrating JSON data. The main text is white on a dark gray
background. The JSON data displays key-value pairs including an 'id' of
'tt7144296', a 'title' of '1. Kiss and Kill', a 'year' of 2017, and a 'rating'
of 2.9. Below the JSON data is a small error message in a light pink box that
says 'Error: Expected: 2.9 Actual: 2.9'. The top of the image contains the
question 'What is the JSON data?' in white text."](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/0/0/0007976ca3410205e4fa403a71b9a1ac79bf5192.png)Screenshot
2025-02-01 132301331×314 12.3 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/0/0/0007976ca3410205e4fa403a71b9a1ac79bf5192.png
"Screenshot 2025-02-01 132301")

  
what is the error here?? sir [@Jivraj](/u/jivraj)



---
**24ds2000024** on 2025-02-01T18:26:06.664Z:

I have the Same doubt.



---
**s.anand** on 2025-02-02T05:30:16.417Z:

[@22f3001315](/u/22f3001315) [@21f3002277](/u/21f3002277)
[@24ds2000024](/u/24ds2000024) – please try again after reloading the page.
The new error message will be clearer, like this:

    
    
    Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4
    

FYI, we expect all values as strings, not numbers. That’s because the year can
sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can
sometimes be missing.



---
**23f2000237** on 2025-02-02T05:41:42.494Z:

In Question 2, it is specifically said to filter the movies however, the
evaluator is expecting a TV show there. Should we also include TV shows now?

edit: This is an everchanging dataset, so will our answers be saved, as, this
json might not be in this order tomorrow?



---
**s.anand** on 2025-02-02T05:45:48.804Z:

[@23f2000237](/u/23f2000237) A good point. Yes, please include _all_ titles.
I’ve reworded the question accordingly. Thanks.



---
**21f3002277** on 2025-02-02T06:31:48.149Z:

Q3. How to handle the error ? [@Jivraj](/u/jivraj)

TypeError: Cannot read properties of null (reading ‘0’)

    
    
    http://127.0.0.1:8000/api/outline?country=Russia
    
    {"outline":"## Contents\n# Russia\n## Etymology\n## History\n### Early history\n### Kievan Rus'\n### Grand Duchy of Moscow\n### Tsardom of Russia\n### Imperial Russia\n#### Great power and development of society, sciences, and arts\n#### Great liberal reforms and capitalism\n#### Constitutional monarchy and World War\n### Revolution and civil war\n### Soviet Union\n#### Command economy and Soviet society\n#### Stalinism and modernisation\n#### World War II and United Nations\n#### Superpower and Cold War\n#### Khrushchev Thaw reforms and economic development\n#### Period of developed socialism or Era of Stagnation\n#### Perestroika, democratisation and Russian sovereignty\n### Independent Russian Federation\n#### Transition to a market economy and political crises\n#### Modern liberal constitution, international cooperation and economic stabilisation\n#### Movement towards a modernised economy, political centralisation and democratic backsliding\n#### Invasion of Ukraine\n## Geography\n### Climate\n### Biodiversity\n## Government and politics\n### Political divisions\n### Foreign relations\n### Military\n### Human rights\n### Corruption\n### Law and crime\n## Economy\n### Transport and energy\n### Agriculture and fishery\n### Science and technology\n#### Space exploration\n### Tourism\n## Demographics\n### Language\n### Religion\n### Education\n### Health\n## Culture\n### Holidays\n### Art and architecture\n### Music\n### Literature and philosophy\n### Cuisine\n### Mass media and cinema\n### Sports\n## See also\n## Notes\n## References\n## Sources\n## Further reading\n## External links"}
    
    

error resolved



---
**22f3001315** on 2025-02-02T10:06:04.746Z:

in my output which is correct  
there are two \n instead of one .



---
**21f3002277** on 2025-02-02T10:38:33.945Z:

it should one(for newline), my code is working now



---
**24ds2000024** on 2025-02-02T11:54:35.123Z:

Dear Sir,  
I was at 2/10 yesterday. After pasting JSON file of IMDB & reloading as
suggested My marks updated to 3/10. Kindly confirm if I have got whole of IMDB
question.



---
**21f3002277** on 2025-02-02T13:00:36.181Z:

Q4. How to handle the error ? [@Jivraj](/u/jivraj)

Error: At 2025-02-05: Values don’t match



---
**23f2003853** on 2025-02-03T00:37:01.721Z:

There is no submit button is available in below screen. Is it fine to save the
link url only. Please clarify (unless we click submit button the log of Graded
Assignment 4 remains red)  

[![Here's alt text for the image: A screenshot shows a computer screen
displaying a graded assignment page for a course at the Indian Institute of
Technology Madras. The page is primarily white with dark gray text and
accents. On the left, a sidebar lists course modules including "Course
Introduction," "Module 1: Development Tools," "Module 2: Deployment Tools,"
"Module 3: Large Language Models," "Project 1," and "Module 4: Data Sourcing."
The main area shows "Graded Assignment 4," with a due date of "2025-02-09,
23:59 IST." Instructions are provided regarding multiple submission attempts
before the deadline, troubleshooting steps if encountering access issues (such
as disabling ad blockers and using Chrome browser), and a student ID
requirement. A link to the assignment is provided:
"https://exam.sanand.workers.dev/tds-2025-01-ga4." The top of the screen shows
the browser's address bar with a portion of a URL visible. The bottom of the
screen shows a Windows taskbar with several application icons. The overall
color scheme is predominantly white and dark gray.](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/6/9/699d94f19d189a93a67fb813a5eeed3d1f73abf3_2_690x388.png)image1920×1080
337 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/6/9/699d94f19d189a93a67fb813a5eeed3d1f73abf3.png
"image")



---
**23f2000237** on 2025-02-03T10:06:13.753Z:

I have a doubt regarding the bonus mark. Suppose someone were to get 10/10 in
the assignment, would their mark be recored as 11/10 or just 10?  
(Assuming they have interacted in this thread)



---
**s.anand** on 2025-02-03T11:16:46.279Z:

Anyone scoring 10/10 on GA4 and replying with a _relevant_ message on this
thread will get 11/10 ![Here's alt text for the image: "A simple, smiling
yellow emoticon. The face is a bright, golden yellow circle with two small,
dark brown or black dots for eyes and a small, upward-curving black line for a
mouth. The background is transparent."](https://emoji.discourse-
cdn.com/google/slight_smile.png?v=12)



---
**23f2003853** on 2025-02-03T11:38:10.970Z:

For me I just made filter of rating between 2 and 7 in site and typed in
console as per video. with that data got in console worked fine.  
copy the coding and save in place use it for data extract when finally submit



---
**22f2000113** on 2025-02-03T16:46:46.395Z:

For question 2 getting Error: At [8].title: Values don’t match. Expected: “9.
Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie
is not found when searched by name  

[![Here's alt text describing the image: "A screenshot shows a search results
page with no results found. On the left, a search filter panel displays
'Search filters' at the top, with the option to 'Expand all'. Below, there are
two filter fields: 'Title name' with the text 'Un matrimonio di troppo'
entered, and 'Title type'. The panel uses light gray and white. On the right,
a grey magnifying glass icon with an 'X' overlaid indicates no search results.
The text 'No results found' is displayed prominently in black, followed by the
instruction 'Please adjust your filters or start a new
search'."](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b7f2ec2868a09d8b4ed3fc50afa02f8416dad93_2_690x143.png)image1414×295
19 KB](https://europe1.discourse-
cdn.com/flex013/uploads/iitm/original/3X/1/b/1b7f2ec2868a09d8b4ed3fc50afa02f8416dad93.png
"image")



---
**nilaychugh** on 2025-02-04T03:28:57.489Z:

how to get the BBC weather API key?



---
**JoelJeffrey** on 2025-02-04T05:47:12.930Z:

Just a quick query on the Bonus mark.

Would this be added to the final grade? Say for example, Someone get a full
score in the first 4 assignments. So the total comes up to 39.5/39.5, and
would be converted to 0.15 or 15 marks. Would the bonus mark be additional to
that 15 or would the score change to 40.5/39.5 and then get normalised to 15?



---
**s.anand** on 2025-02-04T06:15:20.501Z:

[@JoelJeffrey](/u/joeljeffrey) It will be added to the GA4 marks, not the
final grade. So, it’s roughly worth 0.15% on the total - not a full 1% on the
total.



