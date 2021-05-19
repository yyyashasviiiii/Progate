
~ $ pwd                       //  checking present working directory
/home/progate
~ $ mkdir website            //  creating a directory named website
~ $ ls
html       languages  website
~ $ cd website               //  moving from the current directory to website directory
website $ mkdir top          //  creating a directory top inside the directory website
website $ cd top             //  moving to top as the current directory
top $ pwd
/home/progate/website/top
top $ touch top.html          //  creating file top.html inside top directory
top $ touch stylesheet.css    //  creating stylesheet.css file inside top directory
top $ cd
~ $ pwd
/home/progate
~ $ cd website
website $ ls                 //  displaying all the filesa and directories inside website directory
top
website $ cp -r top about    //  copying the directory top and naming the copied directory about
website $ cd about
about $ pwd
/home/progate/website/about
about $ ls
stylesheet.css  top.html
about $ mv top.html about.html   //  renaming the file top.html as about.html
about $ cd
~ $ pwd                           //  moving to the present working directory
/home/progate
~ $ ls
html       languages  website
~ $ touch about.txt             //  crating a file about.txt inside the progate directory
~ $ ls
about.txt  html       languages  website
~ $ rm about.txt                //  removing the newly created file about.txt
~ $ ls
html       languages  website
~ $

                        //            END          //
