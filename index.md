---
layout: default
title: "Welcome to Cryptography"
---

[![Build Status](https://www.travis-ci.com/video-game-coding-club/cryptography.svg?branch=master)](https://www.travis-ci.com/video-game-coding-club/cryptography)

# Introduction

This project contains experiments in cryptography. The goal is to
learn about different cryptographic algorithms.

# Glossary

* Plaintext

    The plaintext is the text we want to encrypt.

* Ciphertext

    The ciphertext is the encrypted plaintext.

* Cipher

    The cryptographic algorithm used to encrypt the plaintext and
    decrypt the ciphertext.

* Cryptographyic Key

    A piece of information that determines the output of the
    cryptographic algorithm (cipher) used. This information is the
    secret that the sender and the recipient need to share.

# Encryption Methods

## Caesar Cipher

In cryptography, a [Caesar
cipher](https://en.wikipedia.org/wiki/Caesar_cipher), also known as
Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is
one of the simplest and most widely known encryption techniques. It is
a type of substitution cipher in which each letter in the plaintext is
replaced by a letter some fixed number of positions down the alphabet.
For example, with a left shift of 3, D would be replaced by A, E would
become B, and so on. The method is named after Julius Caesar, who used
it in his private correspondence.

![Caesar Cipher](assets/Caesar_cipher_left_shift_of_3.svg)

### ROT13

A special case of the Caesar cipher is known as
[ROT13](https://en.wikipedia.org/wiki/ROT13) ("rotate by 13 places",
sometimes hyphenated ROT-13). ROT13 is a simple letter substitution
cipher that replaces a letter with the 13th letter after it.

Because there are 26 letters (2×13) in the basic Latin alphabet, ROT13
is its own inverse; that is, to undo ROT13, the same algorithm is
applied, so the same action can be used for encoding and decoding

![Example for ROT13](assets/ROT13_table_with_example.svg)

# Cryptoanalysis

## Brute Force Attack

In [cryptography](https://en.wikipedia.org/wiki/Cryptography) a
[brute-force attack](https://en.wikipedia.org/wiki/Brute-force_attack)
consists of the attacker trying out all possible keys until the
cleartext is found.

## The Challenge

One day at school you find the following message under your desk. You
suspect that it is encrypted using the Caesar Cipher. Your task is the
following:

1. Decrypt the message
2. Write up what you did to find the cleartext message. This
   description should include more details on the cipher, i.e. the
   shift.
3. As a bonus see if you can find out more about the cleartext.

The write-up should be a simple textfile. Add this textfile to the
repository on GitHub. Then create a pull request against that text
file.

Good luck!

### P.S. A hint

Think about how many keys (i.e. possible shifts) you can chose from
using the Caesar Cipher. One possible way of attacking the ciphertext
is a so called brute-force attack in which you try out all keys until
you find the right one.

### The secret message

	ofoxlopyboroqydovomdbymedon,tkcyxgkcrkfsxqkbyddoxnki.rogyuosxdrolkmuco
	kdypkcmryyvlec,xydcebogroborogkc,ryvnsxqrkxncgsdrkqsbvronsnx'duxyg.drk
	dgkcx'dxomocckbsvidrobyddoxzkbd.droqsbvgkcmedo,ledromyevnx'dpsqeboyedg
	rycrogkcybgrkdrogkcnysxqdrobo.rockdezkxnbellonrscoioc,dbisxqdydrsxu.kp
	ognyjoxusncczbkgvonsxdrocokdcsxpbyxdyprsw,vscdoxsxqdyszync,dkvusxq,ybc
	voozsxq.droikvvvyyuonkbyexnrsckqo...pspdoox?cshdoox?yuki,drkdgkccmkbi.
	ronsnx'duxygrscygxkqo.drolecbewlvonkvyxqklewzibykn.yeddrogsxnygc,nocob
	dbyvvonliexnobklbsqrdlveocui.tkcyxgkczboddiceboronsnx'dvsfosxdronocobd
	.rodbsondydrsxulkmu...drovkcddrsxqrobowowlobon...droqsbvcaeoojonrscrkx
	n."tkcyx,iyeyuki?"crogybopknontokxc,rsusxqlyydc,kxnkpvoomocxyglykbnsxq
	tkmuod.robmrymyvkdolbygxrksbgkcmedmryzzikxnexofox,gsdrdrsxcdbkxnclbksn
	onnygxdrocsnoc.crogyboxywkuoez,vsuocrogkcdbisxqxyddynbkgkddoxdsyxdyrob
	covp;ledsdnsnx'dgybu.crogkccobsyecvizboddi.roboioccoowondymrkxqomyvybv
	suokukvosnycmyzo-lbygx,lveo,kxnqboox.tkcyxvodqyyprobrkxn."ew,snyx'd-"s
	xdropbyxdypdrolec,kdokmrobcryedon,"kvvbsqrd,mezmkuoc,vscdoxez!"droqeig
	kcylfsyecvikmykmr.rsclkcolkvvmkzgkczevvonvygyfobrscrksb,cyiyemyevntecd
	coorscloknioioc.rorknkgscziqykdookxnkcyebpkmo,vsuoro'nokdoxcywodrsxqwy
	vni.rscleppkbwckxnmrocdzecronkqksxcdklbsqrdybkxqozyvycrsbd.rscxivyxgyb
	uyedzkxdckxnxsuocgoboczydvoccgrsdo.kgrscdvorexqpbywrscxomu,kxnkwoqkzry
	xogkcmvszzondyrsclovd.rogyevn'fovyyuonzboddicmkbisprorknx'dlooxpsfopyy
	djoby.groxrocdyynezsxdrokscvo,yxoypdrocdenoxdcmkvvon,"cdkxnez,mykmrron
	qo!""srokbndrkd!"dromykmrcmkxxondrolecpybdroyppoxnob.droxrscoiocpshony
	xtkcyx,kxnrsccmygvnoozoxon.ktyvdgoxdnygxtkcyx'cczsxo.rogkccebodromykmr
	uxogronsnx'dlovyxqdrobo.rogkcqysxqdymkvvtkcyxyed,nowkxngrkdrogkcnysxqy
	xdrolec?kxntkcyxgyevnx'drkfokmveogrkddycki.ledmykmrronqovyyuonkgkikxnm
	vokbonrscdrbykd."go'vvkbbsfosxpsfowsxedoc!cdkigsdriyebzkbdxob.nyx'dvyc
	oiyebgybucrood.kxnspkxiypiyezbomsyecvsddvomezmkuocmkecokxidbyelvoyxdrs
	cdbsz,sgsvvzobcyxkvvicoxniyelkmudymkwzecdrorkbngki."rozsmuonezklkcolkv
	vlkdkxnwknovsuorogkcrsddsxqkrywob.

## Solution Entries

* [Template](template.md)
