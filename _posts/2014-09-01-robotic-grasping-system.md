---
title: Robotic Grasping System Helping the Severely Disabled Take Back Control
date: 2014-09-01
permalink: /posts/2014/09/robotic-grasping-system
excerpt: "Over the past three years, a team of collaborators from New York-Presbyterian..."
tags:
---


Over the past three years, a team of collaborators from New York-Presbyterian/ Columbia University Medical Center, Columbia University, and the University of California/Davis has been developing an assistive robotic grasping platform to enable individuals who are severely disabled to grasp and manipulate objects using novel brain-muscle computer interfaces.


In 2012, the National Science Foundation (NSF) supported the team's collaborative research with a five-year grant as part of an NSF-led national robotics initiative to develop next-generation robotics. "This is more than a technology-driven research endeavor," says Joel Stein, MD, Physiatrist-in-Chief, Department of Rehabilitation Medicine at NewYork-Presbyterian Hospital. "It is also motivated by clinical necessity."

<figure class="pull-right">
	<img src="{{ base_path }}/images/posts/lp_art1_allen_stein.jpg" class="img-responsive"/>
	<figcaption>Drs. Joel Stein and Peter K. Allen with graduate student Jonathan Weisz, who played a key role in the development of the grasping system. (Inset) The subject will be able to confirm a grasp for the handle of the object, such as a detergent bottle.</figcaption>
</figure>


In 2012, the National Science Foundation (NSF) supported the team's collaborative research with a five-year grant as part of an NSF-led national robotics initiative to develop next-generation robotics. "This is more than a technology-driven research endeavor," says Joel Stein, MD, Physiatrist-in-Chief, Department of Rehabilitation Medicine at NewYork-Presbyterian Hospital. "It is also motivated by clinical necessity."

This particular collaboration began when Sanjay Joshi, PhD, an Associate Professor of Mechanical and Aerospace Engineering at the University of California/Davis where he directs the Robotics, Autonomous Systems, and Controls Laboratory, was a visiting professor in the Department of Neurology at Columbia University College of Physicians and Surgeons. At UC/Davis, Dr. Joshi works on surface electromyography (sEMG) – sensors that rely on only a single muscle site. These noninvasive sensors allow people with severe disabilities to communicate through muscle activity – something that is possible because, even though they cannot move their arms or legs, they can send signals to their muscles that can be picked up and can interface with a computer.

At the same time, Peter K. Allen, PhD, Professor of Computer Science at Columbia University, along with Jonathan Weisz, a PhD student in the Columbia University Robotics Group, had developed a user interface that, as Dr. Allen notes, "takes the complexity of grasping and breaks it down into a very simple procedure. The user needs to provide only a few inputs into an intelligent grasping system to direct it to effectively pick things up."

With their combined expertise in robotics, engineering, computer science, and rehabilitative medicine, Drs. Joshi, Allen, and Stein knew they had the makings of an ideal research team. "We realized that we had a sensor, a computer system for grasping, and a client population that would merge very nicely together," says Dr. Allen. It would be a team capable of creating a robotic system that could enable severely disabled people to perform tasks less laboriously, even in a complex, cluttered environment, than is possible with any currently available robotic arms.

### Brain Muscle Computer Interface Grasping System: How it Works
The grasping platform uses a single-signal, multi degree-of-freedom sEMG human robot interface developed by Dr. Joshi. He and his UC/Davis team had previously demonstrated that healthy subjects could learn to navigate a cursor in a two-dimensional space on a screen using modulated sEMG signals obtained over the auricularis superior, the ear wiggling muscle located above the ear, or the extensor pollicis longus, a forearm muscle used to extend the thumb. For placement of the sEMG, they chose the auricularis posterior muscle behind the ear – a location with less hair, making it easier to securely attach the electrode and obtain a strong sEMG signal. The sEMG sensor system is then connected to a computer-driven wheelchair mounted robotic arm.

<h4>Stages in the Grasping Pipeline</h4>
<div class="row">
<div class="col-md-6">
	<ul>
		<li>Object recognition and initialization</li>
		<li>Target selection</li>
		<li>Initial grasp review</li>
		<li>Planner initialization </li>
	</ul>
</div>
<div class="col-md-6">
	<ul>
		<li>On-line grasp refinement</li>
		<li>Final grasp review</li>
		<li>Grasp choice confirmation</li>
	</ul>
</div>
</div>
<div class="row">
	<div class="col-md-6">
		<img src="{{ base_path }}/images/posts/lp_art2_robotic_diagram_2.jpg"/>
		<figcaption>In this phase, the subject sees the planning scene and hits the red target until the object they wish to grasp is highlighted in green.</figcaption>
	</div>
	<div class="col-md-6">
		<img src="{{ base_path }}/images/posts/lp_art2_robotic_diagram.jpg"/>
		<figcaption>After the subject selects the object, the Grasp View pane on the right is populated with a set of grasps from a pre-planned grasp database. A robot hand appears that the user moves to demonstrate a desired starting pose.</figcaption>
	</div>
</div>

"The grasping task is broken down into a multi-stage pipeline that can be navigated with only a few inputs," explains Dr. Allen. "It integrates pre-planned grasps with on-line grasp planning capability." In earlier work at Columbia, Dr. Allen and his group presented a human-in-the-loop grasp planning system using an Emotiv Epoc EEG headset – a low throughput human input device that reads facial gestures and electroencephalography signals.

"We used the Epoc to provide input that demonstrated user intent to a grasp planner who would then plan grasps in near real time," says Dr. Allen. "In our scenario, the user is presented with a live range image of a table with several objects to be grasped and asked to select an object and attempt to lift it off the table using the sEMG interface. We showed with a cohort of five subjects that the interface could be learned in a few 30-minute sessions and that subjects were then able to produce stable grasps for a variety of objects."

An essential aspect of this assistive robotic system will be training patients to use it. "It takes a little time and work for a person to control the sEMG signal accurately," says Dr. Allen. "Although we have a training procedure, it needs to be optimized so rather than taking days for the training, it can be done within minutes. So, we're working on that."

The team is also refining the control mechanisms and engineering details of the system and expect to soon begin clinical testing on a diverse set of patients in the Department of Rehabilitation and Regenerative Medicine at NewYork-Presbyterian/Columbia. Feedback from patients will help refine the system's design and implementation.

In the future, the team may consider other sensors that are capable of providing more information than sEMG sensors, which are now used because they are noninvasive and inexpensive.

"There are a lot of technologies out there that are trying to converge," adds Dr. Allen. "We're currently looking at near-infrared spectroscopy as another type of sensor. By looking at changes in blood flow across the head, you can obtain certain expectation reward signals. It's also possible that we might be able to use more than one sensor together."

But no matter what sensor is ultimately used down the road, Dr. Stein points out, "Whether you're connecting a sensor directly into a brain signal, via a muscle, or using noninvasive brain monitoring, simplifying the tasks for the users is translatable to a variety of different control systems."

### Who Will Benefit
"Right now our target population is patients with spinal cord injuries who have tetraplegia, are cognitively intact, live in the community, and who need help with tasks," says Dr. Stein. "While this is the prime population, potential candidates may include patients with multiple sclerosis, amyotrophic lateral sclerosis, cerebral palsy, muscular dystrophy, and other disorders that impact motor control function. In our clinical studies, we want to identify the 'perfect' patient to substantiate that the principle and the system work so that clinicians can then adapt it to other populations. The surface EMG system works best with a muscle that has normal control. So we have been using muscles that are suitable for the proof of principle thus far and our primary target population would reflect this as well."

However, the team is also looking at people who have difficulty controlling their muscles, such as those who have had strokes affecting one side or both sides of their body. "One project of ongoing exploration is looking at the impact of disorders that affect motor control," says Dr. Stein. "Our preliminary findings show that, in fact, patients with motor control issues do fine with the sEMG sensor…almost as well as people who are able-bodied. This is encouraging in that the assistive robotic system may have wider application beyond those whose target muscles are normal. Ultimately our vision is to have a system that is compact and portable so individuals can use it in their own environment. That's the long-term goal."

<hr>

Single Muscle Site sEMG Interface for Assistive Grasping – presented at the International Conference on Intelligent Robots and Systems (IROS), Chicago, IL, September 14-18, 2014.

Original article [here](http://www.pages01.net/mms/AdvancesinRehabilitationMedecine/rehab_art2_robotic.html).