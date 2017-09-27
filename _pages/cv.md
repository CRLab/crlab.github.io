---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Education
* B.S. in Computer Science, Columbia University, 2016
* M.S. in Computer Science, Columbia University, 2017
* Ph.D in Robotics, Columbia University, 2021 (expected)

## Work experience
<ul>{% for post in site.work %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
## Skills
* Languages: C++, C, Python, OCaml, LaTex, Java, Javascript, HTML/CSS, PHP
* Frameworks known: MongoDB, Graspit!, Moveit!, 
* Tools: Jetbrains, Gitman, Git, Celery

<!-- Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
 -->  
<!-- Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul> -->

## Research
  <ul>{% for post in site.research reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
## Teaching
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
## Service and leadership
* Member of ACM and IEEE

## Interests
* Improvisational humor training from UCB
* Bartending license from Columbia Bartending Agency
