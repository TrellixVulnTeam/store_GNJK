from nltk.corpus import wordnet, wordnet_ic
#List IC file
brown_ic = wordnet_ic.ic('ic-brown.dat')
brown_ic_res = wordnet_ic.ic('ic-brown-resnik.dat')
brown_ic_add1 = wordnet_ic.ic('ic-brown-add1.dat')
semcor_ic_add1 = wordnet_ic.ic('ic-semcor-add1.dat') #IC paling mendekati, berdasarkan Wordnet 3.0
bnc_res = wordnet_ic.ic('ic-bnc-resnik.dat')
bnc = wordnet_ic.ic('ic-bnc.dat')
treebank = wordnet_ic.ic('ic-treebank.dat')

###############################################
dog = wordnet.synset('dog.n.01')
cat = wordnet.synset('cat.n.01')
apple = wordnet.synset('apple.n.01')
pear = wordnet.synset('pear.n.01')
#print("Hasil Similarity Jiang-Conrath:")
#print("(brown_ic) dog dengan cat= " + str(dog.jcn_similarity(cat, brown_ic)))
print("(brown_ic) apple dengan pear= " + str(apple.jcn_similarity(pear, semcor_ic_add1)))
#print("(brown_ic) apple dengan pear= " + str(apple.jcn_similarity(pear, brown_ic_add1)))
#print("(brown_ic) apple dengan pear= " + str(apple.jcn_similarity(pear, brown_ic_res)))
#print("(semcor_ic) apple dengan pear= " + str(apple.jcn_similarity(pear, treebank)))
###############################################

h = wordnet.synset('headset.n.01')
k = wordnet.synset('keyboard.n.01')
#m = wordnet.synsets("monitor")
m = wordnet.synset('monitor.n.04')
c = wordnet.synset('charger.n.02')
s = wordnet.synset('speaker.n.02')
mic = wordnet.synset('microphone.n.01')
#ch = wordnet.synsets("charger")
ch_2 = wordnet.synset('charger.n.02')
#print(ch)
#print(ch_1.hypernyms())
#print(h.hypernyms())
#print(k.hypernyms())
#print(m.hypernyms())
#print(c.hypernyms())
#print(s.hypernyms())
#print(semcor_ic_add1())

print("Headset")
print("headset & keyboard = " + str(h.jcn_similarity(k, semcor_ic_add1)))
print("headset & monitor = " + str(h.jcn_similarity(m, semcor_ic_add1)))
print("headset & charger = " + str(h.jcn_similarity(c, semcor_ic_add1)))
print("headset & speaker = " + str(h.jcn_similarity(s, semcor_ic_add1)))
#print("speaker & mic= " + str(s.jcn_similarity(mic, semcor_ic_add1)))

print("Keyboard")
print("keyboard & monitor = " + str(k.jcn_similarity(m, semcor_ic_add1)))
print("keyboard & charger = " + str(k.jcn_similarity(c, semcor_ic_add1)))
print("keyboard & speaker = " + str(k.jcn_similarity(s, semcor_ic_add1)))

print("monitor")
print("monitor & charger = " + str(m.jcn_similarity(c, semcor_ic_add1)))
print("monitor & spekaer = " + str(m.jcn_similarity(s, semcor_ic_add1)))

print("charger")
print("charger & spekaer = " + str(c.jcn_similarity(s, semcor_ic_add1)))
