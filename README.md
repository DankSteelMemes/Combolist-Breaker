# Combolist-Breaker
Separate the passwords from the email in a combolist of any size, even one that you cannot hold in memory.

Written in Python 3.7 at first.

Python 3.7 takes 51 seconds per 10 million lines.

pypy3 takes 9 seconds per 10 million lines.

I recommend pypy.


This is one of my first Python projects. I know it could be cleaner and 
probably done in a much more efficient way than it is here. That's the 
plan if I ever come back to update this. This will theorhetically work
on any size file. I've tested it on a 10gb file with 260+ million lines
and it worked great. Use an SSD if you are working with large files.


It is made to break a combolist down into a list of passwords.
It isn't perfect but it should give you a list of passwords that are
between 4 and 31 characters long. You can adjust this near the top
of the loop if you want a different set of data. It does its best
to make sure no emails enter the password list. This has a lot to do
with the fact that there were some lines in my list that were reversed
with the email on the right.


It is not worthwhile to have it do a double check of each delimiter
if an error does happen. I tried this with colons with limited success.
For the most part if this cannot separate a string in the first attempt
it isn't going to have much luck after that. There should not be very
many cases where there is a delimiter anywhere near the email or the
beginning of the line.



The try/catch is really only needed because of the print statements
that are now commented out. There was sometimes a unicode error when
printing the offending line that was removed. The file I used this on
was full of weird characters. I'd still keep the try/catch, though.
It will NOT get everything but it does a pretty good job.


Delimters it works with  
    :  
    ;  
    (space)  
    (tab)  
    
It should be fairly easy to add in another type if you would like.

# What needs to be done


    password -> sushsure@email.com    
    Make delimiter section for this. Password is on the wrong side.
    Make this cleaner and maybe bring it all into a function that lets
    you have a list of delimiters instead of too many if statements. Not 
    sure if this is possible as some delimiters need special care while
    others do not. 
    
    Figure out what is best to encode in. Reading the file in latin-1
    was a huge help but encoding back to that isn't great. Encoding 
    into UTF-8 works but I think it is causing many strings to have
    numbers added onto the front. These numbers are possibly 
    representations of characters that cannot be encoded into UTF-8.
    Try to find a way to remove those lines? That might cause the file
    to shrink too much though.
