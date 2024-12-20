# Ask better questions

<p align="center">
  <a href="/README.md">English</a> |
  <a href="/doc/README-zh.md">简体中文</a>
</p>

## Table of Contents

- [Ask better questions](#ask-better-questions)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [V1](#v1)
  - [Plan](#plan)
  - [Good questions are often more important than answers!](#good-questions-are-often-more-important-than-answers)
  - [What is the local optimization trap](#what-is-the-local-optimization-trap)
  - [Types of Doubts](#types-of-doubts)
  - [Core Purpose](#core-purpose)

## Usage

### V1

[pylocal](/pylocal/README.md)

## Plan

1. v1 version, local python verification logic
2. v2 version, web browser plugin one-click integration, allowing users and plugins to communicate to find effective questions. Then jump to gpt communication to find answers.
3. v3 version, users do not need to know gpt. They only need to keep communicating to get answers.

## Good questions are often more important than answers!

Current gpt's are all capable of generating an answer to your question that is pretty much specific to that question. But that's not nearly enough!

Why would we need answers? Because there are doubts.

Types of doubts:
1. clear direction, want to know their direction on the answer, so generate doubts.
2. not clear direction, only know the vague concept, so produce doubt.
3. there is a vague answer inside, and there is some doubt about this answer.

For the three cases:
1. a specific question that has a specific answer (gpt is fine)
2. the second does not produce a direct answer (requires multiple rounds of guidance from gpt), and the degree of depth depends entirely on the quality of the question asked after the person has re-cognized it (**falling into the local optimum trap**)
3. the third kind of elimination of doubts does not mean to provide answers, but to make the person interested in re-cognizing his problems and re-finding new ones. Eventually the answer is found (gpt does not actively inform and the person does not recognize the problem when he is not aware of it, **falling into the local optimum trap**)

## What is the local optimization trap

GPT answer.

> A local optimality trap is a situation in which a decision or algorithm gets stuck on a small range of optimal solutions in the search for an optimal solution to a problem, and fails to find an optimal solution overall. The locally optimal solution performs best on a local scale, but is not optimal globally. The problem usually arises in optimization algorithms, decision making, or strategy planning.
> 
> Features include:
> 1. Locally optimal solutions are restricted to a small area.
> 2. Lack of global view leads to inability to move beyond the local optimum.
> 3. Commonly found in scenarios such as gradient descent, career choice, and business strategy.
> 
> Solutions include:
> 1. using heuristic algorithms to explore a larger solution space.
> 2. Introducing randomness to break the local constraints.
> 3. searching by starting multiple times from different initial points.
> 4. Combining long-term planning to avoid short-term decision constraints.
> 
> The local optimization trap is also prevalent in real life, such as being satisfied with the status quo and neglecting innovation in product design, or being satisfied with the status quo and unwilling to challenge for higher goals in personal growth. Recognizing and attempting to break out of this trap can lead to higher achievement.

This example illustrates it concretely: there is a specific direct answer to the current variety of gpts that are sufficiently available.

## Types of Doubts

We have already listed three types of doubts; the kinds of questions stand in another latitude (quoted from *Writing as a Craft*, which is a chinese book《写作是门手艺》):

| | Big Questions | Small Questions |
|---|---|---|
| Large Meaning | - | - |
| small meaning | - | - |

1. Big questions, big meanings:
   - For example, the philosophical question “How to live a good life?” This question explores the ultimate meaning and purpose of life, and touches on various aspects of self-knowledge, faith, truth, freedom, justice, art, and beauty.
2. Big questions, small meanings:
   - For example, in philosophy, the question “Is there truth?” Although this question may seem grand, in some philosophical schools of thought it may not be directly relevant to the practical applications of everyday life, and therefore its practical significance may be considered relatively small.
3. Small questions, small meanings:
   - For example, the philosophical question “Should man obey the law?” Although this question is very important in law and ethics, from a philosophical point of view, it may be regarded as a more specific and limited question, and its scope and significance may not be as far-reaching as those questions that explore the nature of existence and the universe.
4. Small issues with big implications:
   - For example, the philosophical question “Does man possess free will?” Although this question seems to be a small question about individual choice, it actually touches on deeper issues of human behavior, moral responsibility, and social structure, and has great philosophical significance.

For an individual, how to turn a big problem into a small problem and how to transform a small meaning into a big meaning is the most crucial. Readers can interact with your familiar AI to see if they can get the answers to the above questions.

## Core Purpose

At this point in the line, two core concepts have been expressed: *3 types of confusion* and *4 types of questions*.

The author tends to be confined between the latter two kinds of puzzles, and the questions posed tend to be unspecified. Especially in the author's field of software engineering, to do some technical architecture development, often because of the lack of knowledge, in some old and outdated direction to dig deep, get dusty, and therefore often trapped in a difficult situation.

So the core goal of this project:**Leveraging large language models, pose better questions, and discover better directions.**

Things this project will not do:
1. waste time on features that are already on the market today
2. make a so-called second brain

Things this project will do:
1. make good use of various big models
2. compatible with some mainstream api

Things this project is expected to do:
1. explore whether RAG(Retrieval-Augmented Generation) will optimize the overall experience