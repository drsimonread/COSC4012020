

| Circular Dichroism Spectrometer  Error Log 04/9/21 402 Quality Assurance & Documentation Team |
| :---- |

---

This document’s purpose is to list test results and errors that have been encountered.

**Test:** Sign in/account creation  
**Error:** “ConnectionRefusedError at /accounts/signup/” Error.   
**Fix**: Can now create accounts successfully, email verification appears to function correctly. Forgot password/password change is functional.  
**Resolved(y or n): Yes**

**Test:** Google account sign in  
**Error:** “DoesNotExist at /accounts/google/login/ SocialApp matching query does not exist” Error. Signing in with a Google account via the Google option does not function correctly.  
**Resolved: Yes**

**Test:** Accessibility via web browsers   
Microsoft Edge: y  
Safari: y  
Google Chrome: y  
Firefox: y  
Brave: y  
Internet Explorer: no home page, but everything else yes  
Samsung Internet: y

**Test**: Multigraph function  
**Results**: graph displays with different colors representing different data, graph is overall functional.

**Test**: search function  
**Results**: case sensitive. Users must remember exactly what they called the file or else it won’t be found. Example: when trying to find a file called 40% Roundup Test File, file is not found in search bar if “file” or “test” are written. It would appear you must type in the first word of the file you want or else it will not find the file.  
**Resolved: No**

**Test**: Graph Display  
**Results**: 

* hitting Display over and over keeps adding new color wheels.  
* Changing graph color is not clear, the user is unable to see which graph they are changing the color of.   
* How to apply color change is not clear, the user is unable to see if their selection has been applied. Application appears to occur only after switching graph views. (application occurs in the color wheel with the use of the “selected color” text box, but not on the actual graph.)  
* Changing graph color results in all graphs changing to the same color.

**Resolved: Yes**

**Test**: Data Point Limit (?)  
**Results**:  
List Index Out Range error appears when data points are above 316 in the database. You can upload documents, but cannot view them if there are more than 316 data points in the file. Is there a max number of data points that you can have?(If so, specify)

* though a 1101 data point file (Buffer Test 2\_1) appears to work just fine. Not sure what the error is here.

**Resolved: Yes**

**Test**: Adding a secondary email  
**Results**:  
Template Does Not Exist error appears after clicking confirm email address. A link appears in an email in the secondary email inbox, leads to the website with a button to confirm email address, but then the error page pops up.  
**Resolved: Yes**  
Misc Suggestions

**Test**: Tab Navigation  
**Result**: When switching tabs, the home label states bolded even if you are on a different page  
**Done: Yes**

**Test**: Deletion and/or Permissions  
**Results**: can delete files at current permission level (public, no sign in), delete should be visible on the page (by upload and multigraph) by admin only.  
**Done: Yes**

**Test**: Homepage  
**Results**: opening application immediately displays database, should have proper homepage.  
**Done: Yes**

**Test:** Database viewing page/multi graph button  
**Results:** it is unclear to the user on first seeing the database how to select multiple files to graph. When the multigraph button is selected, nothing happens. It would probably be beneficial to the user to see checkboxes or some indication that they should be selecting files before or when that button is clicked?  
**Done: Yes**

**Test:** “Continue to Website” destination  
**Results:** Currently “Continue to Website” takes you to the About page.  I think it’s more likely that users would want to go to “Index” not “About”  
**Done: Yes**

**Test:** About page readability  
**Results:** This is a wall of text.  No one could find anything.  Please organize into categories and make more readable → some spelling/grammar errors here and there should be fixed as well  
**Done: No**  
