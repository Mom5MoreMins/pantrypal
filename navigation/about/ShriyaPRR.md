---
layout: post
title: Shriyas PRR
description: PRR
menu: nav/about.html
permalink: /about/ShriyaPRR
author: Shriya
comments: true
---

<div style="background-color:rgb(43, 43, 43); border-radius: 15px; padding: 20px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); margin-bottom: 30px; color: black;">

<h1 style="font-size: 28px; color: white; text-align: center;">Checklist Feature Blog</h1>

---

<h2 style="font-size: 22px; color: white; text-align: center;">What is it?</h2>
<p>The Checklist Feature is an interactive tool designed to allow users to add, manage, and track checklist items efficiently.</p>
<p>Unlike the previous Analytics API, which passively collected data, the Checklist API provides direct user engagement by enabling CRUD (Create, Read, Update, Delete) operations on checklist items.</p>


<h1 style="font-size: 28px; color: white; text-align: center;">PPR</h1>


<div style="text-align: center; margin: 20px 0;">
  <img src="{{site.baseurl}}/images/CPT.png" alt="Data in table" style="width: 70%; max-width: 500px; border-radius: 15px; box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2); animation: fadeIn 2s ease-in-out;" />
</div>

<h2 style="font-size: 22px; color: white; text-align: center;">Overview</h2>
<p>My feature allows users to create, manage, and track checklists dynamically through an API, ensuring seamless organization and task management. The system processes online data streams in real time, efficiently handling checklist items while allowing users to interact with them through CRUD operations.</p>

<h2 style="font-size: 22px; color: white; text-align: center;">User Input & Submission</h2>
<ul>
<li>Users can create custom checklists with multiple items. </li>
<li>Each item can be marked as completed, edited, or removed.</li>
<li> Users can mark checklist items as completed or incomplete.</li>
<li>The data is stored and updated in real-time on an AWS-backed database for retrieval.</li>
</ul>

<h2 style="font-size: 22px; color: white; text-align: center;">Backend Processing & CRUD Operations
</h2>
<ul>
<li><b>Create:</b> Users can add checklist items specific to their account.</li>
<li><b>Read:</b> The system fetches and displays the user's checklist in real time.</li>
<li><b>Update:</b> Users can mark checklist items as completed or incomplete.</li>
<li><b>Delete:</b> Users can remove items they no longer need.</li>
</ul>

---

<h2 style="font-size: 22px; color: white; text-align: center;">Features</h2>
<ul>
<li><b>Add Items:</b> Users can input items to their personal checklist. Stored in database via a POST request.</li>
<li><b>Mark Items as Complete:</b> Users can check off items via a PUT request.</li>
<li><b>Delete Items:</b> Users can remove items via a DELETE request.</li>
<li><b>Fetching Items:</b> A GET request retrieves user-specific checklist items.</li>
</ul>


<h2 style="font-size: 22px; color: white; text-align: center;">Student-Developed Procedure (API Delete Method)</h2>
<div style="text-align: center; margin: 20px 0;">
  <img src="{{site.baseurl}}/images/first.png" alt="First" style="width: 70%; max-width: 500px; border-radius: 15px; box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2); animation: fadeIn 2s ease-in-out;" />

</div>

<div class="checklist-container">
    <p style="color: white;">
        The <code>delete(self)</code> function is a Flask route that removes a checklist item from the database, ensuring the user is authenticated with <code>@token_required</code>.
        It retrieves the current user and the JSON request data, checking if an <code>id</code> is provided; otherwise, it returns an error. If the checklist item exists for the user,
        it is deleted from the database, and a success message is returned.
    </p>

<h2 style="font-size: 22px; color: white; text-align: center;">Student-developed procedure being called </h2>
<div style="text-align: center; margin: 20px 0;">
  <img src="{{site.baseurl}}/images/second.png" alt="Second" style="width: 70%; max-width: 500px; border-radius: 15px; box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2); animation: fadeIn 2s ease-in-out;" />

</div>


<div class="checklist-container">
    <p style="color: white;">
        The <code>deleteItem(id)</code> function sends a DELETE request to the backend API to remove a checklist item based on its <code>id</code>.
        It constructs the request using <code>fetch</code>, includes the item’s <code>id</code> in the request body as JSON, and updates the checklist
        by calling <code>fetchChecklistItems()</code>. If an error occurs, it logs the error message to the console, ensuring smooth debugging
        and preventing application crashes.
    </p>

<h2 style="font-size: 22px; color: white; text-align: center;">Initializing Data</h2>
<div style="text-align: center; margin: 20px 0;">
  <img src="{{site.baseurl}}/images/initing.png" alt="Second" style="width: 70%; max-width: 500px; border-radius: 15px; box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2); animation: fadeIn 2s ease-in-out;" />

<div class="checklist-container">
    <p style="color: white;">
        The <code>initChecklist()</code> function initializes a checklist by inserting sample items into a database using SQLAlchemy.
        It loops through a predefined list of dictionaries containing <code>user_id</code> and <code>item_name</code>, creates 
        <code>ChecklistItem</code> objects, adds them to the database session, and commits the changes. This ensures users have 
        default checklist items while demonstrating iteration, data abstraction, and database management for the CSP Create Task.
    </p>
</div>

<style>
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>

<div style="background-color:rgb(49, 49, 49); border-radius: 15px; padding: 20px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); margin-bottom: 30px;">


<h1>AP CSP MCQ Retrospective & Improvement Plan</h1>


<div style="text-align: center; margin: 20px 0;">
  <img src="{{site.baseurl}}/images/mcq.png" alt="AP CSP MCQ Performance Chart" style="width: 80%; max-width: 600px; border-radius: 15px; box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2); animation: fadeIn 2s ease-in-out;" />
</div>



<h2 style="font-size: 24px; color: #7a5dff; text-align: center; border-bottom: 3px solid #7a5dff; padding-bottom: 5px; width: 60%; margin: 20px auto;">Performance Analysis</h2>


<ul style="font-size: 16px; line-height: 1.8; text-align: justify; color: #333; margin-top: 20px;">
<li>After reviewing my <b>AP CSP Practice Exam 1</b> results, I have identified key areas of **strength** and **improvement. My goal is to build on my strong foundation while improving weak areas to maximize my AP exam score.



---


<h2 style="font-size: 22px; color: #28a745; text-align: center;">Strengths: Areas Where I Excelled</h2>


<ul style="font-size: 16px; line-height: 1.8; color: #333; padding-left: 20px;">
  <li><b>Data Representation & Storage:</b> Strong grasp on binary numbers, data compression, and using programs with data.</li>
  <li> <b>Control Structures & Algorithms:</b> High performance in conditionals, loops, and algorithm development.</li>
  <li> <b>Networking & The Internet:</b> Deep understanding of Internet structure, fault tolerance, and parallel computing.</li>
  <li> <b>Computing Ethics & Security:</b> Mastery of computing bias, cybersecurity risks, and legal/ethical concerns.</li>
</ul>


---


<h2 style="font-size: 22px; color: #dc3545; text-align: center;"> Areas for Improvement</h2>


<ul style="font-size: 16px; line-height: 1.8; color: #333; padding-left: 20px;">
  <li> <b>Debugging & Error Correction:</b> Need to improve on identifying and fixing coding errors efficiently.</li>
  <li> <b>Library & API Usage:</b> Struggled with utilizing built-in libraries and understanding documentation.</li>
  <li> <b>Data Abstraction:</b> Need to practice variable usage and function abstraction for cleaner, more efficient code.</li>
</ul>


---


<h2 style="font-size: 24px; color: #007bff; text-align: center; border-bottom: 3px solid #007bff; padding-bottom: 5px; width: 60%; margin: 20px auto;"> Action Plan for Improvement</h2>


<p style="font-size: 16px; line-height: 1.8; text-align: justify; color: #333; margin-top: 20px;">
To improve before the final AP CSP exam, I am working to the following steps:
</p>


<ul style="font-size: 16px; line-height: 1.8; color: #333; padding-left: 20px;">
  <li> <b>Targeted Debugging Practice:</b> Solve coding exercises that require finding and fixing logical errors.</li>
  <li> <b>API Documentation Review:</b>  Work with APIs like Python’s `math` and JavaScript’s `fetch()` to improve function usage.</li> 
  <li> <b>Refactoring Code:</b>  Improve variable usage and abstraction in my projects to follow best coding practices.</li>
</ul>


---


<h2 style="font-size: 24px; color: #ffc107; text-align: center;"> Final Thoughts</h2>


<ul style="font-size: 16px; line-height: 1.8; text-align: justify; color: #333;">
<li>This helped me recognize both my strengths and weaknesses. By focusing on debugging, API usage, and algorithm efficiency , I can ensure that I’m fully prepared for the AP CSP exam.

<style>
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>





<div style="background-color:rgb(49, 49, 49); border-radius: 15px; padding: 20px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); margin-bottom: 30px; color: black;">


<h1 style="font-size: 28px; color: black; text-align: center;">Corrections</h1>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Logic Circuit Analysis</h2>
<p><b>Question:</b> The diagram below shows a circuit composed of three logic gates. Each gate takes two inputs and produces a single output. For which of the following input values will the circuit have an output of <b>true</b>?</p>
<p><b>Answer:</b> C → A = false, B = true, C = true, D = true</p>
<p><b>Why:</b> The OR gate will produce <b>true</b>, and the first AND gate will produce <b>true</b>. Since both inputs to the second AND gate are <b>true</b>, the circuit's output will be <b>true</b>.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Robot Movement Analysis</h2>
<p><b>Question:</b> Do Program I and Program II correctly move the robot to the gray square?</p>
<p><b>Answer:</b> Both Program I and Program II correctly move the robot to the gray square.</p>
<p><b>Why:</b> Both programs successfully navigate the robot through the grid using correct movements and rotations.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Code Correction</h2>
<p><b>Question:</b> A student wrote the following program to remove all occurrences of the strings <b>"the"</b> and <b>"a"</b> from the list <b>wordList</b>. What correction is needed?</p>
<p><b>Answer:</b> Inserting index ← index - 1 between lines 7 and 8.</p>
<p><b>Why:</b> This ensures that the index is decremented after checking each list element, avoiding skipping elements.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Binary Representation</h2>
<p><b>Question:</b> Which of the following can be represented by a sequence of bits?</p>
<p><b>Answer:</b> An integer, an alphanumeric character, and a machine language instruction.</p>
<p><b>Why:</b> All digital data is ultimately represented in sequences of bits.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Spinner Simulation</h2>
<p><b>Question:</b> Which of the following code segments can be used to simulate the behavior of the spinner?</p>
<p><b>Answer:</b> C</p>
<p><b>Why:</b> The code correctly models the probability distribution of the spinner outcomes.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Metadata Storage</h2>
<p><b>Question:</b> Which of the following is least likely to be stored as metadata for a black-and-white image?</p>
<p><b>Answer:</b> A duplicate copy of the data</p>
<p><b>Why:</b> Metadata typically describes the data rather than duplicating it.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Course Grade Calculation</h2>
<p><b>Question:</b> How can a student's course grade be calculated from individual assignment scores?</p>
<p><b>Answer:</b> finalGrade = Sum(scores) - Min(scores); finalGrade = finalGrade / (LENGTH(scores) - 1)</p>
<p><b>Why:</b> This method accounts for dropped lowest scores before calculating the average.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Simulation Complexity</h2>
<p><b>Question:</b> How does removing variables affect the runtime of a simulation?</p>
<p><b>Answer:</b> The updated model is likely to decrease runtime.</p>
<p><b>Why:</b> Simpler models require less computation, reducing runtime.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Binary Search Requirement</h2>
<p><b>Question:</b> What condition must be met for a binary search to work?</p>
<p><b>Answer:</b> The values in <b>numList</b> must be in sorted order.</p>
<p><b>Why:</b> A binary search requires a sorted list to function correctly.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Bit Allocation</h2>
<p><b>Question:</b> What is the minimum number of bits needed to assign unique sequences to 100 staff members?</p>
<p><b>Answer:</b> 7 bits</p>
<p><b>Why:</b> 7 bits allow for up to 128 unique sequences (2^7 = 128).</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Algorithm Complexity</h2>
<p><b>Question:</b> Which of the following algorithms run in reasonable time?</p>
<p><b>Answer:</b> I, II, and III.</p>
<p><b>Why:</b> All three algorithms run in polynomial time, which is considered reasonable.</p>


---


<h2 style="font-size: 22px; color: black; text-align: center;">Execution Time Comparison</h2>
<p><b>Question:</b> How does the execution time compare between Version I and Version II?</p>
<p><b>Answer:</b> Version II requires approximately 5 more minutes than Version I.</p>
<p><b>Why:</b> Version II makes more calls to <b>GetPrediction</b>, increasing execution time from ~4 minutes to ~9 minutes.</p>


</div>


<style>
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>

