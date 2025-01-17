# Python for Public Policy

[![Execute notebooks](https://github.com/afeld/python-public-policy/actions/workflows/main.yml/badge.svg)](https://github.com/afeld/python-public-policy/actions/workflows/main.yml?query=branch%3Amain)

**Alternate course title:** _How to Use a Bit of Code to Do Things That Would Be Really Hard in Spreadsheets_

This repository contains content for [NYU Wagner's Python Coding for Public Policy](https://wagner.nyu.edu/education/courses/python-coding-for-public-policy) class (PADM-GP 4506).

- [Syllabus](syllabus.md#readme)
- [Brightspace site](https://brightspace.nyu.edu/d2l/home/82428), which students will use for:
  - Viewing Announcements
  - Submitting Assignments
  - Viewing grades

Produced and taught by Aidan Feldman. Largely based on [previous iteration by Hannah Kates](https://github.com/hannahkates/python-public-policy).

## Why this class?

There are countless resources out there to learn Python and pandas — books, videos, etc. — and many are free. Relative to other Python/pandas courses, this class:

- Doesn't expect any prior technical experience
- Puts the data/code in a public policy context
  - There's a specific emphasis on learning coding for data analysis rather than software engineering
- Teaches you how to work with open data
- Optimizes for minimal setup

All the lectures and assignment templates are in this repository, so you _could_ go through them on your own. The benefits of enrolling are:

- Additional content
  - You get access to lectures, which includes commentary that isn't in this repository
  - You get access to assignment solutions
- Support
  - There is an instructor to answer questions, both during and between lectures
  - You have peers you can work with
- You invest money and are expected to show up to class and turn in assignments on time, which [makes it far more likely you will complete it](https://mashable.com/2014/12/16/warning-college-may-be-a-waste-of-your-time-and-money/#8BFB_sdkMaqy)

## Assignments

### Tips

- **All lecture slides and homework templates can be found under [`class_materials/`](https://padmgp-4506001-fall.rcnyu.org/user-redirect/notebooks/class_materials/).** The contents of this directory will be automatically updated from [the GitHub repository](https://github.com/afeld/python-public-policy), but should keep any changes you make.
- **Look at the Table of Contents** to get an overview. You can find the Table of Contents button in the sidebar.
- **Read the instructions carefully.** Like word problems from math class, they are very specific in what they are asking for.
- **Spot check your results.** If you are transforming data from a previous Step, compare the results, do a handful of the calculations manually, etc. to ensure that the results are correct.
- **[Don't repeat yourself (DRY).](https://dzone.com/articles/is-your-code-dry-or-wet)** If you find yourself copying and pasting code within a notebook, there's probably a better way to do it.
- Kernel/memory issues
  - If your kernel crashes, let the instructor know.
  - Make sure `Python [conda env:python-public-policy]` is selected as the kernel.
  - Close kernels you aren't using from the [Running](https://padmgp-4506001-fall.rcnyu.org/user-redirect/tree#running) page

### Turning in assignments

1. Ensure all the outputs are visible and the notebook is cleaned up.
   - What you see is what the instructors will see.
1. Leave your name off the notebook filename and the notebook itself, as assignments are graded anonymously.
1. Export the notebook as a PDF. From the Jupyter interface, go to:
   1. `File`
   1. `Download as`
   1. `PDF via LaTeX (PDF)`
1. Upload the PDF to the Brightspace Assignment.

After the resubmission deadline passes for each Assignment, the solutions will be posted in [`shared/solutions/`](https://padmgp-4506001-fall.rcnyu.org/user-redirect/tree/shared/solutions/).

Note: In-class exercises will not be graded.

## Resources

- [Office hours](syllabus.md#instructor-information)
- [Wagner Quantitative Support](https://wagner.nyu.edu/portal/students/academics/advisement/quantitative)
  - Tutoring
  - Math Review
- [NYU Library Data Services](https://library.nyu.edu/departments/data-services/)
  - Consultation
  - Classes
- [Stack Overflow](https://stackoverflow.com/)
- [GitHub Student Developer Pack](https://education.github.com/pack)
  - Includes [learning resources](https://education.github.com/pack?sort=popularity&tag=Learn#offers) and various tools

### Pandas

- [Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- Cheat sheets
  - [Official](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
  - [DataCamp](http://datacamp-community-prod.s3.amazonaws.com/dbed353d-2757-4617-8206-8767ab379ab3)
  - [DataQuest](https://www.dataquest.io/blog/pandas-cheat-sheet/)
- [Python for Data Analysis book](https://bobcat.library.nyu.edu/permalink/f/ci13eu/nyu_aleph003900267)
- NYU's [Quantitative Analysis Guide: Python](https://guides.nyu.edu/quant/python)

There are countless other blog posts, videos, books, etc. out there. There is no "best" resource, as individuals prefer different formats, come in with different experience, and learn at different speeds. Anything that comes up near the top of a Google search will likely be fine.

## Learning more

Want to keep going after this class?

### Python fundamentals

Recommended focusing on fundamentals of Python 3. Many "learn Python" resources will be web development-oriented (they will probably mention [Django](https://www.djangoproject.com/)/[Flask](https://flask.palletsprojects.com/)), so you might want to look for ones that focus on data science or Python 3 on its own. Some that are data-oriented:

- DataCamp's [Python Fundamentals](https://www.datacamp.com/tracks/python-fundamentals) or [Python Programmer](https://www.datacamp.com/tracks/python-programmer) tracks
- [Kaggle's Learn Python tutorials](https://www.kaggle.com/learn/python)

Countless other "learn Python" resources/courses/videos/books out there; there isn't one right choice for everyone.

### Machine learning

- [Kaggle's Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
- [Disco's machine learning content](https://www.heydisco.com/)
- [DataCamp's Natural Language Processing in Python track](https://www.datacamp.com/tracks/natural-language-processing-in-python)

### NYU classes

- [Advanced Data Analytics and Evidence Building](https://wagner.nyu.edu/education/courses/advanced-data-analytics-and-evidence-building)
- [Center for Urban Science + Progress](https://cusp.nyu.edu/masters-degree/curriculum/)
  - Applied Data Science
  - Machine Learning for Cities

## See also

- [14 Principles of Open Government Data](https://opengovdata.io/2014/principles/)
- [Blog post about GitHub for non-developers](https://medium.com/nyc-planning-digital/git-what-extolling-githubs-virtues-to-non-coders-6cc11f1a5fd2)

## Testimonials

> This class has been extremely helpful and my only regret is that I didn't take it sooner in my NYU career. … In fact, I've already put python to use for my final thesis. … In writing my thesis, I used python for descriptive statistics that would have otherwise taken much longer in excel … Writing code for these analysis probably saved me about a day or two of work.

---

> Thank you for an incredible semester. I truly took away a lot that I feel will help me dive deeper into a career in public service, while having unique skills that will help me deliver a much greater impact into the communities I'm serving.

---

> The in-class assignments and homework provided many opportunities to practice the Python concepts we learned in class. … Professor Feldman was able to present difficult concepts in a way that was easy to digest as someone who knew very little about Python prior to this course. This course achieved its goal of removing the uneasiness I felt towards Python and coding in general, and for a 7-week course, that is no easy feat!

---

> Everything controllable by the professor was fantastic. The objectives were straightforward and value-added. The professor helped make sure that we were coming away from assignments with real tangible understanding of the code rather than focusing on completion. I was challenged, but the professor was always around to answer questions.
