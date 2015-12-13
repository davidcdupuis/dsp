# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>> * **pwd**      : print working directory
  
>> * **hostname** : print name of computer
  
>> * **mkdir**    : make directory (-m, --mode, = MODE ; set permission mode (chmod) | -p, --parents; make parent directories as needed)

>> * **cd**       : change directory

>> * **rmdir**    : remove directory (```rm -R -- */``` : remove directory and all sub-directories; -r, -R, --recursive)

>> * **pushd**    : takes current directory and "pushes" it into a list for later, then it changes to another directory (```pushd new_directory```)

>> * **popd**     : takes the last directory you "pushed" and "pops" it off, taking you back there (```popd```)

>> * **touch**    : used to make empty files (```touch file.txt```)

>> * **cp**       : copy (```cp file1.txt file2.txt``` -f to delete existing target file; -r to recursively copy all of the content of one directory to another)

>> * **mv**       : moving / renaming files (```mv <old_name> <new_name>```)

>> * **less**     : used to view (but not change) the contents of a text file one screen at a time. Similar to "more" but has the extended capability of allowing both forward and backward navigation through the file. ("less is more", press ```q``` to quit)

>> * **cat**      : reads files sequentially, writing them to standard output

>> * **rm**       : remove a file

>> * **gzip**     : compress a file into a .gz format (```gzip <file_name>```, to decompress us ```gzip -d <file_name>``` this will delete the compacted version)

>> * **tar**      : create, add files to, or extract files from an archive file in gnutar format, called a tarfile 

>>> - ```tar -cvf <file.tar> <directory>``` :  create a tar archive file for a directory in current working directory; 

>>>>> c : creates a new. tar archive file; 

>>>>> v : verbosely show the .tar file progress; 

>>>>> f : filename of the archive file

>>> - ```tar cvzf <file.tar> <directory>``` : create a compressed gzip archive file with `z`

>>> - ```tar -xvf <file_name.tar>``` or ```tar -xvf <file_name.tar> -C <directory>``` to untar tar file

>>>>> x  : extract

>>>>> -c : untar in different directory

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>> **ls** : list directory

>>> * -a, --all : do not hide entries starting with `.`
>>> * -C : list entries by column
>>> * -l : use a long listing format
>>> * -h : print sizes in human readable format

---


---

What does `xargs` do? Give an example of how to use it.

>> **xargs** : used to build and execute command lines from standard input. It allows the fetching of the arguments used in the command. It helps avoid long commands that may otherwise not function, such as: 

```
[command]|while read param
do
[process]
done
```

>> instead one will have : ```[command]|xargs [process]```

>> ex: "rm 'find /path -type f' won't work instead we will use "find /path -type f -print | xargs rm"

>> In this example the `find` utility feeds the input of `xargs` with a long list of file names. `xargs` then splits this list into sublists and call `rm` once for every sublist.

>> **XARGS is a sort of `for loop` for the command line**

---

