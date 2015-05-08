
MWSimi
======

This Python script trawls through the pages in a MediaWiki installation and identifies pages which are similar.

The primary use case for this program is in large enterprise deployments, where different parts of the organisation might be creating MW content with similar purpose. Diligent use of this script helps the MW caretakers to improve the synergistic effects of using a Wiki platform by identifying efforts which should be consolidated.

MWSimi uses Natural Language Processing to determine similarity. Specifically, the algorithm employed is [Term Frequency-Inverse document Frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

Installation
============

MYSimi runs in an embedded and interactive IPython session. You are strongly encouraged to run PYSimi in a Python virtualenv since that is how it is developed.

A requirements.txt is distributed along with MWSimi for installation of MWSimi dependencies.

Usage
=====

    (mwsimi)josef@debian:src$ python mwsimi.py 
    Python 2.7.3 (default, Mar 14 2014, 11:57:14) 
    Type "copyright", "credits" or "license" for more information.
    
    IPython 3.1.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.
    
    In [1]: dev.loadpages?
    Signature: dev.loadpages(min_length=None, **kwargs)
    Docstring:
    loads all pages into an instance variable and calculates similarities
    
    Keyword arguments:
    min_length -- used to exclude very small pages which can often trigger false positives
    prefix -- select only pages starting with string
    namespace -- select only pages in namespace (integer as string)
    
    Other keyword arguments, see the mwclient.allpages docstring at:
    htwtps://github.com/mwclient/mwclient/blob/87d525fd24db3546f8b2b9d1ffa1dc50975911cc/mwclient/client.py#L565
    File:      ~/Documents/development/environments/mwsimi/src/mwsimi.py
    Type:      instancemethod
    
    In [2]: 

Rights
======

This program is licensed under ther MIT License Copyright Josef Assad 2015.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
