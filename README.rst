Neurotopics
===========

Authors: Jessica Mollick, Tim Rubin, L. Amber Wilcox-O'Hearn

Contact: jmollick@gmail.com, timrubin@indiana.edu, amber@cs.toronto.edu

Released under the GNU AFFERO GENERAL PUBLIC LICENSE, see COPYING file for details.

Introduction
============

Neurotopics is a topic modelling tool for `NeuroSynth`_.
We will take a Neurosynth dataset, a brain atlas in NIFTI or Analyze
format, and a file containing word frequency counts for all words in
the documents of the dataset.
For each ROI in the atlas, we will generate a distribution on a subset of the words.

Dependencies
============

* Python
* `NeuroSynth`_


Sparse Matrix Formatting
========================
The formatting of the docwfreqs file uses a sparse matrix format which is efficient for  storing large text files (because a Word x Document matrix is highly sparse). 
Each row represents a document.
Within each row, the document's word-counts are formatted as follows:

wordID:wordCOUNT wordID:wordCOUNT ....

So for each unique word-type in the document, there will be a pair of numbers separated by a colon, indicating:
(1) wordID; the identifier for the word-type, which maps to the strings in the vocab-list file
(2) wordCOUNT; the number of times the wordID occurred in the document (i.e. the number of tokens of wordID in the doc)

Toy Example:
------------
Suppose our vocab list was:

0	brain
1	function
2	eye
3	vision
4	pizza
5 	tacos

Now suppose we had a document with the following tokens (ignoring order)

brain eye eye eye eye pizza tacos tacos tacos

In the docwfreqs file it would look like this:

0:1 2:4 4:1 5:3



.. _NeuroSynth: https://github.com/NeuroSynth
