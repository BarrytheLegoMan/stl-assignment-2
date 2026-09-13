# Stage 1 Lab - Human vs AI: Building Your First SmartCare Prototype
## Part A Understand the Problem

### What data must be stored?
There will be multiple database tables: one table to record patient details, with attributes such as Unique Patient Number, First Name, Last Name, Address, Contact No., Emergency Contact, etc. There is a Practitioner table that will include the employee number, First Name, Last Name, and scheduled work availability. In this instance, there is a separate table for appointment times. This table will have a composite foreign key made up of patient number and Employee number, along with the appointment date and time, the room of service, or an online comment for room preparation.
### What functions might be useful?
Functions to check whether patient details already exist in the system before creating a new Patient. An ability to confirm the available time slot before booking the appointment. A Function to make the practitioner available for appointments. A way to set the office Public Holiday schedule 
### What could go wrong?
Data cleansing, practice, and organisation, especially if it is a paper-based system, to digitise the record. The document mentions spreadsheet tracking, which is unstructured data and may not be recorded with the same level of detail as the system specification. 
### What requirements are unclear?
Whether the patient's primary key will be their Medicare number or the clinic's own record-keeping. In what system does the clinic currently store practitioner details, and is there integration with the existing dataset? Or starting new

## Part B - Build a Human-Written Prototype
1. In the basic input and output, it is all hard-coded; no input is taken from the user
2. In a similar way, the data type is not recorded in the program, so no safeguard for bad input data
3. Because it is manual entry, there is no cross-referencing of existing data; the Practitioner name would be repeated over and over again
4. While the list has a value error if the patient name is empty, the other attributes can be created missing
5. The Raise Value error: maybe give more details in the program; if the user doesn't know where to look, it may not help

## Part E
| Question                     | Human version | AI version |
|------------------------------|---------------|------------|
| Easy to understand?          | 	yes           | 	Somewhat   |
| Runs successfully?           | 	yes           | 	Yes        |
| Uses only required features? | 	maybe         | 	Maybe      |
| Adds assumptions?	            | No            | 	yes        |
| Handles errors?	              | No            | 	No         |
| Could I explain it?	          | yes           | 	kinda      |

## Part F 
Normal Appointment - Length of Appointment and Appointment type not set
Blank patient name - Neither version stops the creation of a blank name record
Two appointments for the same practitioner/time - Nothing is checked for creating appointments at the same time, except the list, and the exact details couldn't be added twice.
Strange input such as patient_name=None or appointment_time=None - There was no validation on record types or how they were saved, so funky inputs were possible.

## Part G - Improve One Thing
A single controlled improvement is to validate that the patient name is not empty.

## Part H - Reflection
### What did you build before using AI?
My career so far has been on the operational side of administration. I am studying business informatics and have a focus on project management. My coding experience has been limited to the unit of study within my university degree. I have been involved in the product development lifecycle and development systems and processes with developers to improve work practices. 
### What did AI help you understand?
AI has an understanding of the syntax in an area, while I get skills
### Did AI make assumptions?
I think there were educated assumptions, based on its learnt knowledge. There was a difference between putting the prompt in the new chat and running it in the chat after having it review the code provided in this document
### How did you verify the AI output?
I applied my knowledge of doing UAT and BVT in the workplace to come up with tests. When we get to acceptance criteria, we will have more information to build out features.
### What engineering work remained for you?
Working with the Business Analyst and System Analyst, forming and storming requirements collection and bug fixing in complex situations, whether there are multiple factors in an IT environment and challenges of imposed limitations. 