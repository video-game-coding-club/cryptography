---
layout: default
title: "Welcome to Cryptography"
---

[![Build Status](https://www.travis-ci.com/video-game-coding-club/cryptography.svg?branch=master)](https://www.travis-ci.com/video-game-coding-club/cryptography)

Please check out [the deployed webpage](https://video-game-coding-club.github.io/cryptography/).

# Introduction

This project contains experiments in cryptography. The goal is to
learn about different cryptography algorithms and their
implementation.

# Encrypt a plain text message

<table style="width:100%">
  <tr>
    <td>
      <div id="algorithm">
        <select>
          <option value="cesar">Cesar Cipher</option>
        </select>
      </div>
    </td>
  </tr>
  <tr>
    <td>
      <div id="plaintext">
        <textarea rows="4" cols="80">
Please enter your plaintext message and then press the Encrypt button
below...
        </textarea>
      </div>
    </td>
  </tr>
  <tr>
    <td>
      <button type="button">Encrypt!</button>
    </td>
  </tr>
</table>
