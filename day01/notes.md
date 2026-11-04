1. What is a manifest?
A manifest is a file that stores information about the dataset rows, such as their IDs, source, timestamp, status, label, and whether they are trainable. It helps us keep track of which rows are allowed for training and which are not.


2. Why do rejected rows stay in the file?
Rejected rows stay in the file so that we don't lose any original dataset information. Even if a row is not suitable for training, we still keep it for tracking, checking, and future reference. We simply mark it as trainable: false.


3. Why does the second run get a new folder?
The second run gets a new folder so that the results from the first run are not overwritten. This helps us keep both runs separate and compare their outputs whenever needed.


4. Which two statuses are trainable, and why is unmatched not one of them?
Only matched and no_positive are considered trainable statuses. A matched row has a valid match, while no_positive represents a case where no positive match was found. unmatched is not trainable because it does not meet either of the two allowed status conditions.