Note: Install node.js from http://nodejs.org/ for building the app.


For Issue #697 (this is a severe regression bug)

> The key step to repro this bug:

1. open a bible book and scroll up to the first chapter

2. long click on the text at the very beginning 

3. click the pen icon on the menu bar to create a note with content (e.g., "hello"), and save the note

4. reopen the note via the pen icon in the verse (the note is empty, this is already a sign error, the first error stack trace appears)

5. input new content (e.g., "world"), and save (press back key to save), the current page shows "An error has occurred. Report a bug" (the second stack trace appears). 

6. go to the main menu and click the note option, the app crashes (the third AndroidRuntime stack trace appears).


For Issue #261:

> The user has to download a bible first and then download a book before he can go to view the book.

For Issue #480:

> The basic functionality of creating and modifying labels is correct.
The crash can be triggered only when the first label was created and deleted it. 
After the crash happens, the basic functionality cannot be used anymore (i.e.,
modifying labels will just crash). In addition, We find the crash can be reproduced
when renaming the empty labels (do not need to do the remaining steps in the bug report).

 
