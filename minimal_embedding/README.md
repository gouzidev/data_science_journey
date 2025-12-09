

# minimal sentence embedding with glove

so this is just a small project i did to see how close two sentences are, like, in meaning. i use glove word vectors (the 50d ones, i think?) and just average the vectors for each word in a sentence, then do cosine similarity. not sure if this is the best way but it kinda works lol

## what is this?

basically, i grab the glove vectors, tokenize the sentence, and for each word i get its vector (if it exists, sometimes it doesnt). 
then i just take the mean of all those vectors and thats my sentence vector. then i use cosine similarity to see how close two sentences are. its pretty simple, maybe too simple but it works tho

## how to run it

first you need to install the stuff:

```
pip install -r req.txt
```

then just run the notebook:

```
jupyter notebook notebook.ipynb
```

or you can use the init script:

```
./init.sh
```

the notebook should download the glove file for you if you dont have it, so you dont need to push it or anything. if it doesnt work, maybe the link is down or something, idk

## how it works (i think)

1. download and load the glove 50d word vectors
2. tokenize sentences and get the mean vector for each
3. calculate cosine similarity between sentence vectors to see how close they are
4. print some similarity scores for example sentences

## dependencies

- numpy
- requests
- jupyter

## files

- `notebook.ipynb` - main notebook with all the code and examples
- `glove.6B.50d.txt` - glove word vectors (should be downloaded automatically)
- `req.txt` - dependencies
- `init.sh` - setup and run script
