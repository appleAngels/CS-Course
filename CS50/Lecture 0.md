### CS50 - Introduction to the intellectual enterprises of computer science and the art of programming

DAVID MALAN: All right, this is CS50, Harvard University's introduction to the intellectual enterprises of computer science and the art of programming, back here on campus in beautiful Sanders Theatre for the first time in quite a while.
So welcome to the class.
My name is David — OK.
[CHEERING AND APPLAUSE]
So my name is David Malan.
And I took this class myself some time ago, but almost didn't.
It was sophomore fall and I was sitting in on the class.
And I was a little curious but, eh, it didn't really feel like the field for me.
I was definitely a computer person, but computer science felt like something altogether.
And I only got up the nerve to take the class, ultimately, because the professor at the time, Brian Kernighan, allowed me to take the class pass/fail, initially.
And that is what made all the difference.
I quickly found that computer science is not just about programming and working in isolation on your computer.
It's really about problem solving more generally.
And there was something about homework, frankly, that was, like, actually fun for perhaps the first time in, what, 19 years.
And there was something about this ability that I discovered, along with all of my classmates, to actually create something and bring a computer to life to solve a problem, and sort of bring to bear something that I'd been using every day but didn't really know how to harness, that's been gratifying ever since, and definitely challenging and frustrating.
Like, to this day, all these years later, you're going to run up against mistakes, otherwise known as bugs, in programming, that just drive you nuts.
And you feel like you've hit a wall.
But the trick really is to give it enough time, to take a step back, take a break when you need to.
And there's nothing better, I daresay, than that sense of gratification and pride, really, when you get something to work, and in a class like this, present, ultimately, at term's end, something like your very own final project.
Now, this isn't to say that I took to it 100% perfectly.
In fact, just this past week, I looked in my old CS50 binder, which I still have from some 25 years ago, and took a photo of what was apparently the very first program that I wrote and submitted, and quickly received minus 2 points on.
But this is a program that we’ll soon see in the coming days that does something quite simply like print "Hello, CS50," in this case, to the screen.
And to be fair, I technically hadn't really followed the directions, which is why I lost those couple of points.
But if you just look at this, especially if you've never programmed before, you might have heard about programming language but you've never typed something like this out, undoubtedly it's going to look cryptic.
But unlike human languages, frankly, which were a lot more sophisticated, a lot more vocabulary, a lot more grammatical rules, programming, once you start to wrap your mind around what it is and how it works and what these various languages are.
It’s so easy, you'll see, after a few months of a class like this, to start teaching yourself, subsequently, other languages, as they may come, in the coming years as well.
So what ultimately matters in this particular course is not so much where you end up relative to your classmates but where you end up relative to yourself when you began.
And indeed, you'll begin today. And the only experience that matters ultimately in this class is your own.
And so, consider where you are today.
Consider, perhaps, just how cryptic something like that looked a few seconds ago.
And take comfort in knowing just some months from now all of that will be within your own grasp.
And if you're thinking that, OK, surely the person in front of me, to the left, to the right, behind me, knows more than me, that's statistically not the case.
2/3 of CS50 students have never taken a CS course before, which is to say, you're in very good company throughout this whole term.
So then, what is computer science?
I claim that it's problem solving.
And the upside of that is that problem solving is something we sort of do all the time.
But a computer science class, learning to program,I think kind of cleans up your thoughts.
It helps you learn how to think more methodically, more carefully, more correctly, more precisely.
Because, honestly, the computer is not going to do what you want unless you are correct and precise and methodical.
And so, as such, there’s these fringe benefits of just learning to think like a computer scientist and a programmer.
And it doesn't take all that much to start doing so.
This, for instance, is perhaps the simplest picture of computer science, sure, but really problem solving in general.
Problems are all about taking input, like the problem you want to solve.
You want to get the solution, a.k.a. output.
And so, something interesting has got to be happening in here, in here, when you're trying to get from those inputs to outputs.
Now, in the world of computers specifically, we need to decide in advance how we represent these inputs and outputs.
We all just need to decide, whether it's Macs or PCs or phones or something else, that we're all going to speak some common language, irrespective of our human languages as well.
And you may very well know that computers tend to speak only what language, so to speak?
Assembly, one, but binary, two, might be your go-to.
And binary, by implying two, means that the world of computers has just two digits at its disposal, 0 and 1.
And indeed, we humans have many more than that, certainly not just zeros and ones alone.
But a computer indeed only has zeros and ones. And yet, somehow they can do so much.
They can crunch numbers in Excel, send text messages, create images and artwork and movies and more.
And so, how do you get from something as simple as a few zeros, a few ones, to all of the stuff that we're doing today in our pockets and laptops and desktops?
Well, it turns out that we can start quite simply. If a computer were to want to do something as simple as count, well, what could it do?
Well, in our human world, we might count doing this, like 1, 2, 3, 4, 5, using so-called unitary notation, literally the digits on your fingers where one finger represents one person in the room, if I'm, for instance, taking attendance.
Now, we humans would typically actually count 1, 2, 3, 4, 5, 6.
And we'd go past just those five digits and count much higher, using zeros through nines.
But computers, somehow, only have these zeros and ones.
So if a computer only somehow speaks binary, zeros and ones, how does it even count past the number 1?
Well, here are 3 zeros, of course.
And if you translate this number in binary, 000, to a more familiar number in decimal, we would just call this zero.
Enough said.
If we were to represent, with a computer, the number 1, it would actually be 001, which, not surprisingly, is exactly the same as we might do in our human world, but we might not bother writing out the two zeros at the beginning.
But a computer, now, if it wants to count as high as two, it doesn't have the digit 2.
And so it has to use a different pattern of zeros and ones. And that happens to be 010.So this is not 10 with a zero in front of it.
It's indeed zero one zero in the context of binary.
And if we want to count higher now than two, we're going to have to tweak these zeros and ones further to get 3.
And then if we want 4 or 5 or 6 or 7, we’re just kind of toggling these zeros and ones, a.k.a. bits, for binary digits that represent, via these different patterns, different numbers that you and I, as humans, know, of course, as the so-called decimal system, 0 through 9, dec implying 10, 10 digits, those zeros through nine.
So why that particular pattern?
And why these particular zeros and ones?
Well, it turns out that representing one thing or the other is just really simple for a computer.
Why? At the end of the day, they’re powered by electricity.
And it's a really simple thing to just either store some electricity or don't store some electricity.
Like, that's as simple as the world can get, on or off. 1 or 0, so to speak.
So, in fact, inside of a computer, a phone, anything these days that's electronic, pretty much, is some number of switches, otherwise known as transistors.
And they're tiny. You've got thousands, millions of them in your Mac or PC or phone these days.
And these are just tiny little switches that can get turned on and off.
And by turning those things on and off in patterns, a computer can count from 0 on up to 7, and even higher than that.
And so these switches, really, you can think of being as like switches like this.
Let me just borrow one of our little stage lights here.
Here's a light bulb. It's currently off.
And so, I could just think of this as representing, in my laptop, a transistor, a switch, representing 0.
But if I allow some electricity to flow, now I, in fact, have a 1.
Well, how do I count higher than 1? I, of course, need another light bulb. So let me grab another one here.
And if I put it in that same kind of pattern, I don't want to just do this.
That's sort of the old finger counting way of unary, just 1, 2.
I want to actually take into account the pattern of these things being on and off.
So if this was one a moment ago, what I think I did earlier was I turned it off and let the next one over be on, a.k.a. 010.
And let me get us a third bit, if you will. And that feels like enough.
Here is that same pattern now, starting at the beginning with 3.
So here is 000. Here is 001. Here is 010, a.k.a., in our human world of decimal, 2.
And then we could, of course, keep counting further.
This now would be 3 and dot dot dot.
If this other bulb now goes on, and that switch is turned and all three stay on— this, again, was what number?

AUDIENCE: Seven.

DAVID MALAN: OK, so, seven.
So it's just as simple, relatively, as that, if you will. But how is it that these patterns came to be?
Well, these patterns actually follow something very familiar.
You and I don't really think about it at this level anymore because we've probably been doing math and numbers since grade school or whatnot.
But if we consider something in decimal, like the number 123, I immediately jump to that. This looks like 123 in decimal. But why?
It's really just three symbols, a 1, a 2 with a bit of curve, a 3 with a couple of curves, that you and I now instinctively just assign meaning to.
But if we do rewind a few years, that is one hundred twenty-three because you're assigning meaning to each of these columns.
The 3 is in the so-called ones place. The 2 is in the so-called tens place. And the 1 is in the so-called hundreds place. And then the math ensues quickly in your head.
This is technically 100 times 1, plus 10 times 2, plus 1 times 3, a.k.a. 100 plus 20 plus 3.
And there we get the sort of mathematical notion we know as 123. Well, nicely enough, in binary, it's actually the same thing.
It's just these columns mean a little something different.
If you use three digits in decimal, and you have the ones place, the tens place, and the hundreds place, well, why was that 1, 10, and 100?
They're technically just powers of 10. So 10 to the 0, 10 to the 1, 10 to the 2.
Why 10? Decimal system, "dec" meaning 10.
You have 8 and 10 digits, 0 through 9.
In the binary system, if you’re going to use three digits, just change the bases if you’re using only zeros and ones.
So now it's powers of 2, 2 to the 0, 2 to the 1, 2 to the 2, a.k.a. 1 and 2 and 4, respectively.
And if you keep going, it's going to be 8s column, 16s column, 32, 64, and so forth.
So, why did we get these patterns that we did?
Here's your 000 because it's 4 times 0, 2 times 0, 1 times 0, obviously 0.
This is why we got the decimal number 1 in binary.
This is why we got the number 2 in binary, because it's 4 times 0, plus 2 times 1, plus 1 times 0, and now 3, and now 4, and now 5, and now 6, and now 7.
And, of course, if you wanted to count as high as 8, to be clear, what do you have to do? What does a computer need to do to count even higher than 7?

AUDIENCE: Add a bit.

DAVID MALAN: Add a bit. Add another light bulb, another switch.
And, indeed, computers have standardized just how many zeros and ones, or bits or switches, they throw at these kinds of problems.
And, in fact, most computers would typically use at least eight at a time.
And even if you're only counting as high as three or seven, you would still use eight and have a whole bunch of zeros.
But that's OK, because the computers these days certainly have so many more, thousands, millions of transistors and switches that that's quite OK.
All right, so, with that said, if we can now count as high as seven or, frankly, as high as we want, that only seems to make computers useful for things like Excel, like number crunching.
But computers, of course, let you send text messages, write documents, and so much more.
So how would a computer represent something like a letter, like the letter A of the English alphabet, if, at the end of the day, all they have is switches?
Any thoughts?
Yeah.

AUDIENCE: You can represent letters in numbers.

DAVID MALAN: OK, so we could represent letters using numbers.
OK, so what's a proposal? What number should represent what?

AUDIENCE: Say if you were starting at the beginning of the alphabet, you could say 1 is A, 2 is B, 3 is C.

DAVID MALAN: Perfect.
Yeah, we just all have to agree somehow that one number is going to represent one letter.
So 1 is A, 2 is B, 3 is C, Z is 26, and so forth.
Maybe we can even take into account uppercase and lowercase.
We just have to agree and sort of write it down in some global standard.
And humans, indeed, did just that. They didn't use 1, 2, 3. It turns out they started a little higher up.
Capital A has been standardized as the number 65. And capital B has been standardized as the number 66. And you can kind of imagine how it goes up from there.
And that's because whatever you're representing, ultimately, can only be stored, at the end of the day, as zeros and ones.
And so, some humans in a room before, decided that capital A shall be 65, or, really, this pattern of zeros and ones inside of every computer in the world, 01000001.
So if that pattern of zeros and ones ever appears in a computer, it might be interpreted then as indeed a capital letter A, eight of those bits at a time.
But I worry, just to be clear, we might have now created a problem.
It might seem, if I play this naively, that, OK, how do I now actually do math with the number 65?
If now Excel displays 65 is an A, let alone Bs and Cs.
So how might a computer do as you've proposed, have this mapping from numbers to letters, but still support numbers?
It feels like we've given something up.
Yeah?

AUDIENCE: By having a prefix for letters?

DAVID MALAN: By having a prefix?

AUDIENCE: You could have prefixes and suffixes.

DAVID MALAN: OK, so we could perhaps have some kind of prefix, like some pattern of zeros and ones--
I like this-- that indicates to the computer here comes another pattern that represents a letter.
Here comes another pattern that represents a number or a letter.
So, not bad. I like that. Other thoughts?
How might a computer distinguish these two? Yeah.

AUDIENCE: Have a different file format, so, like, odd text or just check the graphic or--

DAVID MALAN: Indeed, and that's spot-on.
Nothing wrong with what you suggested, but the world generally does just that.
The reason we have all of these different file formats in the world, like JPEG and GIF and PNGs and Word documents, .docx, and Excel files and so forth, is because a bunch of humans got in a room and decided, well, in the context of this type of file, or really, more specifically, in the context of this type of program, Excel versus Photoshop versus Google Docs or the like, we shall interpret any patterns of zeros and ones as being maybe numbers for Excel, maybe letters in, like, a text messaging program or Google Docs, or maybe even colors of the rainbow in something like Photoshop and more.
So it's context dependent.
And we'll see, when we ourselves start programming, you the programmer will ultimately provide some hints to the computer that tells the computer, interpret it as follows.
So, similar in spirit to that, but not quite a standardized with these prefixes.
So this system here actually has a name ASCII, the American Standard Code for Information Interchange.
And indeed, it began here in the US, and that’s why it's actually a little biased toward A's through Z’s and a bit of punctuation as well.
And that quickly became a problem.
But if we start simply now, in English, the mapping itself is fairly straightforward.
So if A is 65, B it 66, and dot dot dot, suppose that you received a text message, an email, from a friend, and underneath the hood, so to speak, if you kind of looked inside the computer, what you technically received in this text or this email happened to be the numbers 72, 73, 33, or, really, the underlying pattern of zeros and ones.
What might your friend have sent you as a message, if it's 72, 73, 33?

AUDIENCE: Hey.

DAVID MALAN: Hey? Close.

AUDIENCE: Hi.

DAVID MALAN: Hi. It's, indeed, hi. Why?
Well, apparently, according to this little cheat sheet, H is 72, I is 73.
It's not obvious from this chart what the 33 is, but indeed, this pattern represents "hi." And anyone want to guess, or if you know, what 33 is?

AUDIENCE: Exclamation point.

DAVID MALAN: Exclamation point. And this is, frankly, not the kind of thing most people know.
But it's easily accessible by a nice user-friendly chart like this.
So this is an ASCII chart.
When I said that we just need to write down this mapping earlier, this is what people did.
They wrote it down in a book or in a chart.
And, for instance, here is our 72 for H, here is our 73 for I, and here is our 33 for exclamation point.
And computers, Macs, PCs, iPhones, Android devices, just know this mapping by heart, if you will.
They've been designed to understand those letters.
So here, I might have received "hi." Technically, what I've received is these patterns of zeros and ones.
But it's important to note that when you get these patterns of zeros and ones in any format, be it email or text or a file, they do tend to come in standard lengths, with a certain number of zeros and ones altogether.
And this happens to be 8 plus 8, plus 8. So just to get the message "hi, exclamation point,” you would have received at least, it would seem, some 24 bits.
But frankly, bits are so tiny, literally and mathematically, that we don't tend to think or talk, generally, in terms of bits.
You're probably more familiar with bytes.
B-Y-T-E-S is a byte, is a byte, is a byte. A byte is just 8 bits.
And even those, frankly, aren’t that useful if we do out the math.
How high can you count if you have eight bits?
Anyone know? Say it again? Higher than that.
Unless you want to go negative, that's fine. 256, technically 255.
Long story short, if we actually got into the weeds of all of these zeros and ones, and we figured out what 11111111 mathematically adds up to in decimal, it would indeed be 255, or less if you want to represent negative numbers as well.
So this is useful because now we can speak, not just in terms of bytes but, if the files are bigger, kilobytes is thousands of bytes, megabytes is millions of bytes, gigabytes is billions of bytes, terabytes are trillions of bytes, and so forth.
We have a vocabulary for these increasingly large quantities of data.
The problem is that, if you're using ASCII and, therefore, eight bits or one byte per character, and originally, only seven, you can only represent 255 characters.
And that's actually 256 total characters, including zero.
And that's fine if you're using literally English, in this case, plus a bunch of punctuation.
But there's many human languages in the world that need many more symbols and, therefore, many more bits.
So, thankfully, the world decided that we'll indeed support not just the US English keyboard, but all of the accented characters that you might want for some languages.
And heck, if we use enough bits, zeros and ones, not only can we represent all human languages in written form, as well as some emotions along the way, we can capture the latter with these things called emojis.
And indeed, these are very much in vogue these days.
You probably send and/or receive many of these things any given day.
These are just characters, like letters of an alphabet, patterns of zeros and ones that you're receiving, that the world has also standardized.
For instance, there are certain emojis that are represented with certain patterns of bits.
And when you receive them, your phone, your laptop, your desktop, displays them as such.
And this newer standard is called Unicode. So it's a superset of what we called ASCII.
And Unicode is just a mapping of many more numbers to many more letters or characters, more generally, that might use eight bits for backwards compatibility with the old way of doing things with ASCII, but they might also use 16 bits.
And if you have 16 bits, you can actually represent more than 65,000 possible letters.
And that's getting up there.
And heck, Unicode might even use 32 bits to represent letters and numbers and punctuation symbols and emojis.
And that would give you up to 4 billion possibilities. And, I daresay, one of the reasons we see so many emojis these days is we have so much room.
I mean, we've got room for billions more, literally.
So, in fact, just as a little bit of trivia, has anyone ever received this decimal number, or if you prefer binary now, has anyone ever received this pattern of zeros and ones on your phone, in a text or an email, perhaps this past year?
Well, if you actually look this up, this esoteric sequence of zeros and ones happens to represent face with medical mask.
And notice that if you've got an iPhone or an Android device, you might be seeing different things.
In fact, this is the Android version of this, most recently.
This is the iOS version of it, most recently.
And there's bunches of other interpretations by other companies as well.
So Unicode, as a consortium, if you will, has standardized the descriptions of what these things are.
But the companies themselves, manufacturers out there, have generally interpreted it as you see fit.
And this can lead to some human miscommunications.
In fact, for like, literally, embarrassingly, like a year or two, I started being in the habit of using the emoji that kind of looks like this because I thought it was like woo, happy face, or whatever.
I didn't realize this is the emoji for hug because whatever device I was using sort of looks like this, not like this.
And that's because of their interpretation of the data.
This has happened too when what was a gun became a water pistol in some manufacturers' eyes.
And so it's an interesting dichotomy between what information we all want to represent and how we choose, ultimately, to represent it.
Questions, then, on these representations of formats, be it numbers or letters, or soon more.
Yeah?

AUDIENCE: Why is decimal popular for a computer if binary is the basis for everything?

DAVID MALAN: Sorry, why is what so popular?

AUDIENCE: Why is the decimal popular if binary is the fundamental--

DAVID MALAN: Yeah, so we'll come back to this in a few weeks, in fact.
There are other ways to represent numbers.
Binary is one. Decimal is another. Unary is another.
And hexadecimal is yet a fourth that uses 16 total digits, literally 0 through 9 plus A, B, C, D, E, F. And somehow, you can similarly count even higher with those.
We'll see in a few weeks why this is compelling. But hexadecimal, long story short, uses four bits per digit.
And so, four bits, if you have two digits in hex, that gives you eight.
And it's just a very convenient unit of measure.
And it's also human convention in the world of files and other things.
But we'll come back to that soon. Other questions?

AUDIENCE: Do the lights on the stage supposedly say that--

DAVID MALAN: Do the lights on the stage supposedly say anything?
Well, if we had thought in advance to use maybe 64 light bulbs, that would seem to give us 8 total bytes on stage, 8 times 8, giving us just that.
Maybe.
Good question. Other questions on 0's and 1's? It's a little bright in here.
No? Oh, yes? Where everyone's pointing somewhere specific.
There we go. Sorry. Very bright in this corner.

AUDIENCE: I was just going to ask about the 255 bits, like with the maximum characters.
[INAUDIBLE]

DAVID MALAN: Ah, sure, and we’ll come back to this, in some form, in the coming days too, at a slower pace too, we have, with eight bits, two possible values for the first and then two for the next, two for the next, and so forth.
So that's 2 times 2 times 2.
That's 2 to the eighth power total, which means you can have 256 total possible patterns of zeros and ones.
But as we'll see soon computer scientists, programmers, software often starts counting at 0 by convention and if you use one of those patterns, 00000000 to represent the decimal number we know is zero, you only have 255 other patterns left to count as high as therefore 255.
That's all. Good question.
All right, so what then might we have besides these emojis and letters and numbers?
Well, we of course have things like colors and programs like Photoshop and pictures and photos.
Well let me ask the question again.
How might a computer, do you think, knowing what you know now, represents something like a color?
Like what are our options if all we’ve got are zeros and ones and switches?
Yeah?

AUDIENCE: RGB

DAVID MALAN: RGB. RGB indeed is this acronym that represents some amount of red and some amount of green and blue and indeed computers can represent colors by just doing that.
Remembering, for instance, this dot.
This yellow dot on the screen that might be part of any of those emojis these days, well that's some amount of red, some amount of green, some amount of blue.
And if you sort of mix those colors together, you can indeed get a very specific one.
And we'll see you in just a moment just that.
So indeed earlier on, humans only used seven bits total.
And it was only once they decided, well, let's add an eighth bit that they got extended ASCII and that was initially in part a solution to the same problem of not having enough room, if you will, in those patterns of zeros and ones to represent all of the characters that you might want.  
But even that wasn't enough and that’s why we've now gone up to 16 and 32 and long past 7 bits.
So if we come back now to this one particular color. RGB was proposed as a scheme, but how might this work? Well, consider for instance this.
If we do indeed decide as a group to represent any color of the rainbow with some mixture of some red, some green, and some blue, we have to decide how to represent the amount of red and green and blue.

> simplify the problem  
> rainbow -> seven colors -> rgb(red, green, blue)

Well, it turns out if all we have are zeros and ones, `ergo` numbers, let's do just that.

For instance, suppose a computer we’re using, these three numbers 72, 73, 33, no longer in the context of an email or a text message, but now in the context of something like Photoshop, a program for editing and creating graphical files, maybe this first number could be interpreted as representing some amount of red, green, and blue, `respectively`.

And that's exactly what happens. You can think of the first digit as red, second as green, third as blue.
And so ultimately when you combine that amount of red, that amount of green, that amount of blue, it turns out it’s going to resemble `the shade of yellow`.

> rgb(red, green, blue) -> rgb(72, 73, 33) -> shade yellow

And indeed, you can `come up with` a numbers between 0 and 255 for each of those colors to mix any other color that you might want.

And you can actually see this in practice.
Even though our screens, `admittedly`, are getting really good on our phones and laptops such that you `barely` see the dots, they are there.

You might have heard the `term` _pixel_ before.

Pixel's just a dot on the screen and you’ve got thousands, millions of them these days `horizontally` and `vertically`.

If I take even this emoji, which again happens to be one company's interpretation of a face with `medical mask` and `zoom` in a bit, maybe zoom in a bit more, you can actually start to see these pixels.
Things get `pixelated` because what you're seeing is each of the `individual` dots that `compose` this particular image.

And apparently each of these individual dots are probably using `24 bits`, _eight bits for red, eight bits for green, eight bits for blue_, in some pattern.

This program or some other like Photoshop is interpreting one pattern and it's white or yellow or black or some brown in between.
So if you look sort of `awkwardly`, but up close to your phone or your laptop or maybe your TV, you can see exactly this, too.

All right, well, what about things that we also watch every day on YouTube or the like?
Things like videos. How would a computer, knowing what we know now, represent something like a video?
How might you represent a video using only zeros and ones? Yeah?

AUDIENCE: As we can see here, they represent images, right? Sounds of the 0 and 1s as well.

[INAUDIBLE]

DAVID MALAN: Yeah, exactly. To `summarize`, what video really adds is just some notion of time. It's not just one image, it’s not just one letter or a number, it's `presumably` some kind of `sequence` because time is passing.

So with a whole bunch of images, maybe 24 maybe 30 per second, if you fly them by the human's eyes, we can interpret them using our eyes and brain that there is now movement and therefore video.
Similarly with audio or music.

If we just `came up with` some `convention` for representing those same notes on a musical `instrument`, could we have the computer `synthesize` them, too?

And this might be actually pretty familiar.

Let me pull up a quick video here, which happens to be an old school version of the same idea. You might remember from childhood.

So `granted` that particular video is an actual video of a paper-based `animation`, but indeed, that's really all you need, is some sequence of these images, which themselves of course are just zeros and ones because they’re just this `grid` of these pixels or dots.

Now something like `musical notes` like these, those of you who are `musicians` might just naturally play these on physical devices, but computers can certainly represent those sounds, too.

> people play piano -> pc represent sounds

For instance, a popular format for audio is called MIDI and MIDI might just represent each note that you saw a moment ago `essentially` as a sequence of numbers.

But more `generally`, you might think about music as having notes, for instance, A through G, maybe some `flats` and some `sharps`, you might have the `duration` like how long is the note being heard or played on a piano or some other device, and then just the `volume` like how hard does a human in the real world press down on that key and therefore how loud is that sound?

> the type of notes, how long and hard(loud) the note playe

It would seem that just remembering little details like that `quantitatively` we can then represent really all of these otherwise `analog` human `realities`.

So that then is really `a laundry list of ways` that we can just represent information.

Again, computers or digital have all of these different formats, but at the end of the day and `as fancy as` those devices in years are, it's just zeros and ones, tiny little switches or light bulbs, if you will, represented in some way and `it's up to` the software that you and I and others write to use those zeros and ones in ways we want to get the computers to do something more powerfully.

> we do sth powerfully by using software, it's just 0 and 1s, represent in different ways

Questions, then, on this representation of information, which I daresay is ultimately what problem solving is all about, taking in information and producing new (information) `via some process` in between.

> input -> process / function -> output

Any questions there? Yeah, in back.

AUDIENCE: Yeah, so we talked about how different file formats kind of allow you to interpret information. How does a file format like .mp4 `discriminate` between audio and video within itself as a value?

DAVID MALAN: So a really good question. There are many other file formats out there.
You `allude` to MP4 for video and more generally the use are these things called `codecs` and `containers`.
It's not quite as simple when using larger files, for instance, in more modern formats that a video is just a sequence of images, for instance.
Why?

If you stored that many images for like a Hollywood movie, like 24 or 30 of them per second, that's a huge number of images.

> 24 images/second * 60 seconds * 120 minutes

And if you've ever taken photos on your phone, you might know how many megabytes or larger even individual `photographs` might be.

So humans have developed over the years a `fancier software` that uses much more math to represent the same information more minimally just using somehow shorter patterns of zeros and ones than are most simplistic representation here.

> same information -> minimally zeros and ones

And they use what might be called `compression`.

If you've ever used a zip file or something else, somehow your computer is using fewer zeros and ones to represent the same amount of information, `ideally` without losing any information.

In the world of `multimedia`, which we’ll `touch on` a little bit in a few weeks, there are both `lossy` and `lossless` formats out there.

Lossless means you lose no information whatsoever.

But more commonly as you're `alluding` to one is lossy compression, L-O-S-S-Y, where you're actually throwing away some amount of quality.

You're getting some amount of `pixelation` that might not look perfect to the human, but heck it's a lot cheaper and a lot easier to `distribute`.

And in the world of multimedia, you have containers like QuickTime and other MPEG containers that can combine different formats of video, different formats of audio in one file, but there, too, do designers have `discretion`.So more in a few weeks, too.

Other questions, then, on information here as well?
Yeah?

AUDIENCE: So I know computers used to be very big and taking up like a whole room and stuff. Is the reason they've gotten smaller because we can store this information `piecemeal` or what?

DAVID MALAN: Exactly. I mean, `back in the day` you might have heard of the expression `a vacuum tube`, which is like some `physically` large device that might have only stored some 0 or 1.
Yes, it is the `miniaturization` of hardware these days that has allowed us to store as many and many more zeros and ones much more closely together.

> vacuum tube (large and store less) -> miniaturization

And as we've built more `fancy` machines that can sort of design this hardware at an even smaller `scale`, we're just `packing` more and more into these devices.

But there, too, is a `trade off`. For instance, you might know by using your phone or your laptop `for quite a while`, maybe on your `lap`, starts to get warm.

So there are these literal physical `side effects` of this where now some of our devices run hot.

This is why like a data center in the real world might need more `air conditioning` than a typical place, because there are these physical `artifacts` as well.

In fact, if you'd like to see one of the earliest computers from `decades` ago, across the river here in now Allston in the new engineering building is the *Harvard Mark 1 computer* that will give you a much better `mental model` of just that.

Well if we come back now to this first picture being computer science or really problem solving, I daresay we have more than enough ways now to represent information, input and output, so long as we all just agree on something and thankfully all of those before us have given us things like ASCII and Unicode.

> information represent -> ASCII, Unicode

`Not to mention` MP4s, word documents, and the like.

But what's inside of this `proverbial` black box into which these inputs are going in, the outputs are coming?

Well that's where we get this term you might have heard, too.

An `algorithm`, which is just step-by-step `instructions` for solving some problem `incarnated` in the world of computers by software.

> algorithm -> software in computer -> step-by-step instructions

When you write software aka programs, you are `implementing` one or more algorithms, one or more sets of instructions for solving some problem, and maybe you're using this language or that, but `at the end of the day`, no matter the language you use, the computer is going to represent, what you type, using just zeros and ones.

> at the end of the day -> finally, in a word

So what might be a `representative` algorithm?

Nowadays you might use your phone `quite a bit` to make calls or send texts or emails and therefore you have a whole bunch of contacts in your address book.

Nowadays, of course, this is very digital, but whether on iOS or Android or the like, you might have a whole bunch of names, first name and/or last, as well as numbers and emails and the like.

You might be in the habit of like scrolling through on your phone all of those names to find the person you want to call.

It's probably sorted alphabetically by first name or last name, A through Z, or some other symbol.

This is frankly quite the same as we used to do back in my day, CS50, when we just used a physical book.

In this physical book might be a whole bunch of names alphabetically sorted from left to right corresponding to a whole bunch of numbers.

So suppose that in this old Harvard phone book we want to search for John Harvard.

We might of course start quite simply at the beginning here, looking at one page at a time, and this is an algorithm.

This is like literally step-by-step looking for the solution to this problem.

In that sense, if John Harvard's in the phone book, is this algorithm page-by-page correct, would you say?

AUDIENCE: Yes.

DAVID MALAN: Yes.

Like if John Harvard’s in the phone book, obviously I'm eventually going to get to him, so that's what we mean by correct.
Is it efficient? Is it well designed, would you say? No.

I mean this is going to take forever even just to get to the Js or the Hs, depending how this thing's sorted.
All right, well let me go a little faster.
I'll start like two pages at a time. 2, 4, 6, 8, 10, 12, and so forth. Sounds faster, is faster, is it correct?

AUDIENCE: No.

DAVID MALAN: OK, why is it not correct? Yeah?

AUDIENCE: So if you’re starting on page 1, you're only going odd number of pages, so if it's on an even number page, you'll miss it.

DAVID MALAN: Exactly.
If I start on an odd number of pages and I'm going two at a time I might miss pages in between.
And if I therefore conclude when I get to the back of the book there was no John Harvard, I might have just errored.
This would be again one of these bugs. But if I try a little harder, I feel like there's a solution. We don't have to completely throw out this algorithm.
I think we can probably go roughly twice as fast still. But what should we do instead to fix this? Yeah, in back.

AUDIENCE: [INAUDIBLE]

DAVID MALAN: Nice.
So I think what many of us, most of us, if we even use this technology any more these days, we might go roughly to the middle of the phone book just to kind of get us started.
And now I'm looking down, I'm looking for J, assuming first name, J Harvard, and it looks like I'm in the M section.
So just to be clear, what should I do next?

AUDIENCE: [INAUDIBLE]

DAVID MALAN: OK, and presumably it is John Harvard would be to the left of this.
So here's an opportunity to figuratively and literally tear this particular problem in half, throw half of the problem away.
It's actually pretty easy if you just do it that way.
The hard way is this way. But I've now just decreased the size of this problem really in half.
So if I started with 1,000 pages of phone numbers and names, now I'm down to 500.
And already we haven’t found John Harvard, but that's a big bite out of this problem.
I do think it's correct because if J is to the left of M, of course, he's definitely not going to be over there.
I think if I repeat this again dividing and conquering, if you will, here I might have gone a little too far. Now I'm in like the E section.
So let me tear the problem in half again, throw another 250 pages away, and again repeat, dividing and dividing and conquering until finally, presumably, I end up with just one page of a phone book on which John Harvard’s name either is or is not, but because of the algorithm you proposed, step by step, I know that he's not in anything I discarded.
So traumatic is that might have been made out to be, it's actually just harnessing pretty good human intuition.
Indeed, this is what programming is all about, too.
It's not about learning a completely new world, but really just how to harness intuition and ideas that you might already have and take naturally but learning how to express them now more succinctly, more precisely, using things called programming languages.
Why is an algorithm like that if I found John Harvard better than, ultimately, just doing the first one or even the second and maybe doubling back to check those even pages?
Well let's just look at little charts here.
Again, we don't have to get into the nuances of numbers, but if we've got like a chart here, xy plot, on the x-axis here I claim as the size of the problem.
So measured in the numbers of pages in the phone book.
So the farther you go out here, the more pages are in the phone book.
And here we have time to solve on the y-axis.
So the higher you go up, the more time it’s going to be taking to solve that particular problem.
So let's just arbitrarily say that the first algorithm, involving like n pages, might be represented graphically like this.
No matter the slope, it's a straight line because there's presumably a one to one relationship between numbers of pages and number of seconds or number of page turns.
Why?
If the phone company adds another page next year because some new people move to town, that’s going to require one additional page for me.
One to one.
If, though, we use the second algorithm, flawed though it was, unless we double back a little bit to fix someone being in between, that's too going to be a straight line, but it’s going to be a different slope because now there's a 2 to 1 or a 1 to 2 relationship because I’m going to pages at a time.
So if the phone company adds another page or another two pages, that still only just one more step.
You can see the difference if I kind of draw this.
If this is the phone book in question, this number of pages, it might take this many seconds on the yellow line to represent or to find someone like John Harvard.
But of course on the first algorithm, the red line, it's literally going to take twice as many steps.
And what do the n here mean?
n is the go-to variable for computer scientist or programmer just generically representing a number.
So if the number of pages in the phone book is n, the number of steps the second algorithm would have taken would be in the worst case n over 2.
Half as many because you're going twice as fast.
But the third algorithm, actually if you recall your logarithms, looks a little something like this.
There's a fundamentally different relationship between the size of the problem and the amount of time required to solve it that technically is log-based, too, again, but it's really the shape that's different.
The implication there is that if, for instance, Cambridge and Allston, two different towns here in Massachusetts, merge next year and there's just one phone book that's twice as big, no big deal for that third and final algorithm.
Why?
You just tear the problem one more time in half, taking one more byte, that's it, not another 1,000 bytes just to get to the solution.
Put another way, you can walk it way, way, way out here to a much bigger phone book and ultimately that green line is barely going to have budged.
So this then is just a way of now formalizing and thinking about what the performance or quality of these algorithms might be.
Before we now make one more formalization of the algorithm itself, any questions then on this notion of efficiency or now performance of ideas?
Yeah.

AUDIENCE: How many phone books have you got?

DAVID MALAN: (LAUGHING) A lot of phone books over the years and if you or your parents have any more still somewhere we could definitely use them because they're hard to find.
Other questions? But thanks.
Other questions here, too? No. Oh, was that a murmur? Yes, over here.

AUDIENCE: You could get Harry Potter as a guest speaker.

DAVID MALAN: Sorry, say again.

AUDIENCE: You could get Harry Potter as a guest speaker.

DAVID MALAN: (LAUGHING) Oh, yeah. Hopefully.
Then we'd have a little something more to use here.
So now if we want to formalize further what it is we just did, we can go ahead and introduce this.
A form of code aka pseudocode.
Pseudocode is not a specific language, it's not like something we're about to start coding in, it’s just a way of expressing yourself in English or any human language succinctly correctly toward an end of getting your idea for an algorithm across.
So for instance, here might be how we could formalize the code, the pseudocode for that same algorithm.
Step one was pick up the phone book, as I did.
Step two might be open to the middle of the phone book, as you proposed that we do first.
Step three was probably to look down at the pages, I did.
And step four gets a little more interesting because I had to quickly make a decision and ask myself a question.
If person is on page, then I should probably just go ahead and call that person.
But that probably wasn't the case at least for John Harvard, and I opened the M section.
So there's this other question I should now ask else if the person is earlier in the book, then I should tear the problem in half as I did but go left, so to speak, and then not just open to the middle of the left half of the book, but really just go back to step three, repeat myself.
Why?
Because I can just repeat what I just did, but with a smaller problem having taken this big bite.
But, if the person was later in the book, as might have happened with a different person than John Harvard, then I should open to the middle of the right half of the book, again go back to line three, but again, I’m not going to get sucked doing something forever like this because I keep shrinking the size of the problem.
Lastly, the only possible scenario that’s left, if John Harvard is not on the page and he's not to the left and he's not to the right, what should our conclusion be?

AUDIENCE: He's not there.

DAVID MALAN: He's not there. He's not listed. So we need to quit in some other form.
Now as an aside, it's kind of deliberate that I buried that last question at the end because this is what happens all too often in programming, whether you're new at it or professional, just not considering all possible cases, corner cases if you will, that might not happen that often, but if you don't anticipate them in your own code, pseudocode or otherwise, this is when and why programs might crash or you might say stupid little spinning beach balls or hourglasses or your computer might reboot.
Why?
It's doing something sort of unpredictable if a human, maybe myself, didn't anticipate this.
Like what does this program do if John Harvard is not in the phone book if I had omitted lines 12 and 13? I don't know.
Maybe it would behave differently on a Mac or PC because it's sort of undefined behavior.
These are the kinds of omissions that frankly you're invariably going to make, bugs you're going to introduce, mistakes you're going to make early on, and me, too, 25 years later.
But you'll get better at thinking about those corner cases and handling anything that can possibly go wrong and as a result, your code will be all the better for it.
Now the problem ultimately with learning how to program, especially if you've never had experience or even if you do but you learned one language only, is that they all look a little cryptic at first glance.
But they do share certain commonalities.
In fact, we'll use this pseudocode to define those first.
Highlighted in yellow here are what henceforth we're going to start calling functions.
Lots of different programming languages exist, but most of them have what we might call functions, which are actions or verbs that solve some smaller problem.
That is to say, you might use a whole bunch of functions to solve a bigger problem because each function tends to do something very specific or precise.
These then in English might be translated in code, actual computer code, to these things called functions.
Highlighted in yellow now are what we might call conditionals.
Conditionals are things that you do conditionally based on the answer to some question.
You can think of them kind of like forks in the road.
Do you go left or go right or some other direction based on the answer to some question?
Well, what are those questions?
Highlighted now in yellow or what we would call Boolean expressions, named after a mathematician last name Bool, that simply have yes no answers.
Or, if you prefer, true or false answers or, heck, if you prefer 1 or 0 answers.
We just need to distinguish one scenario from another.
The last thing manifests in this pseudocode is what I might highlight now and call loops.
Some kind of cycle, some kind of directive that tells us to do something again and again so that I don't need a 1,000-line program to search a 1,000-page phone book, I can get away with a 13-line program but sort of repeat myself inherently in order to solve some problem until I get to that last step.
So this then is what we might call pseudocode and indeed there are other characteristics of programs that we'll touch on before long, things like arguments and return values, variables, and more, but unfortunately in most languages, including some we will very deliberately use in this class and that everyone in the real world these days still uses, its programs tend to look like this.
This for instance, is a distillation of that very first program I wrote in 1996 in CS50 itself just to print something on the screen.
In fact, this version here just tries to print quote unquote, "Hello, world." Which is, dare say, the most canonical first thing that most any programmer ever gets a computer to say just because, but look at this mess.
I mean, there's a hash symbol, these angled brackets, parentheses, words like int, curly braces, quotes, parentheses, semicolons, and back slashes.
I mean there's more overhead and more syntax and clutter than there is an actual idea.
Now that's not to say that you won't be able to understand this before long, because honestly there's not that many patterns, indeed programming languages have typically a much smaller vocabulary than any actual human language, but at first it might indeed look quite cryptic.
But you can perhaps infer I have no idea what these other lines do yet, but "Hello, world." is presumably quote unquote what will be printed on the screen.
But what we'll do today, after a short break, and set the stage for next week is introduce these exact same ideas in just a bit using Scratch, something that you yourselves might have used when you're quite younger but without the same vocabulary applied to those ideas.
The upside of what we'll soon do using Scratch, this graphical programming language from our friends down the road at MIT, it'll let us today start to drag and drop things that look like puzzle pieces that interlock together if it makes logical sense to do so, but without the distraction of hashes, parentheses, curly braces, angle brackets, semicolons, and things that are quite beside the point.
But for now, let's go ahead and take a 10 minute break here and when we resume, we will start programming.
So this on the screen is a language called C something that will dive into next week and thankfully this now on the screen is another language called Python that we'll also take a look at in a few weeks before long along with other languages along the way.
Today though, and for this first week, week zero, so to speak, we use Scratch because again it will allow us to explore some of those programming fundamentals that will be in C and in Python and in JavaScript and other languages, too, but in a way where we don't have to worry about the distractions of syntax.
So the world of Scratch looks like this.
It's a web-based or downloadable programming environment that has this layout here by default. On the left here we'll soon see is a palette of puzzle pieces, programming blocks that represent all of those ideas we just discussed.
And by dragging and dropping these puzzle pieces or blocks over this big area and connecting them together, if it makes logical sense to do so, we’ll start programming in this environment.
The environment allows you to have multiple sprites, so to speak.
Multiple characters, things like a cat or anything else, and those sprites exist in this rectangular world up here that you can full screen to make bigger and this here by default is Scratch, who can move up, down, left, right and do many more things, too.
Within its Scratch’s world you can think of it as perhaps a familiar coordinate system with Xs and Ys which is helpful only when it comes time to position things on the screen.
Right now Scratch is at the default, 0,0, where x equals 0 and y equals 0.
If you were to move the cat way up to the top, x would stay zero, y would be positive 180.
If you move the cat all the way to the bottom, x would stay zero, but y would now be negative 180.
And if you went left, x would become negative 240 but y would stay 0, or to the right x would be 240 and y would stay zero.
So those numbers generally don’t so much matter because you can just move relatively in this world up, down, left, right, but when it comes time to precisely position some of these sprites or other imagery, it’ll be helpful just to have that mental model off up, down, left, and right.
Well let's go ahead and make perhaps the simplest of programs here.
I'm going to switch over to the same programming environment now for a tour of the left hand side.
So by default selected here are the category in blue motion, which has a whole bunch of puzzle pieces or blocks that relate to motion.
And whereas Scratch as a graphical language categorizes things by the type of things that these pieces do, we'll see that throughout this whole palette we'll have functions and variables and conditionals and Boolean expressions and more each in a different color and shape.
So for instance, moving 10 steps or turning one way or the other would be functions categorized here as things like motion.
Under looks in purple, you might have speech bubbles that you can create by dragging and dropping these that might say "hello" or whatever for some number of seconds.
Or you could switch costumes, change the cat to look like a dog or a bird or anything else in between.
Sounds, too.
You can play sounds like "meow" or anything you might import or record, yourself.
Then there's these things Scratch calls events and the most important of these is the first, when green flag clicked.
Because if we look over to the right of Scratch's world here, this rectangular region has this green flag and red stop sign up above, one of which is for Play one of which is for Stop and so that's going to allow us to start and stop our actual programs when that green flag is initially clicked.
But you can listen for other types of events when the spacebar is pressed or something else, when this sprite is clicked or something else.
Here you already see like a programmer's incarnation of things you and I take for granted like every day now on our phones.
Any time you tap an icon or drag your finger or hit a button on the side.
These are what a programmer would call events, things that happen and are often triggered by us humans and things that a program be it in Scratch or Python or C or anything else can listen for and respond to.
Indeed, that's why when you tap the phone icon on your phone, the phone application starts up because someone wrote software that's listening for a finger press on that particular icon.
So Scratch has these same things, too.
Under Control in orange, you can see that we can wait for one second or repeat something some number of times, 10 by default, but we can change anything in these white circles to anything else.
There's another puzzle piece here forever, which implies some kind of loop where we can do something again and again.
Even though it seems a little tight, there's not much room to fit something there, Scratch is going to have these things grow and shrink however we want to fill similarly shaped pieces.
Here are those conditionals.
If something is true or false, then do this next thing.
And that's how we can put in this little trapezoid-like shape.
Some form of Boolean expression, a question with a yes/no, true/false, or one/zero answer and decide whether to do something or not.
You can combine these things, too.
If something is true, do this, else do this other thing.
And you can even tuck one inside of the other if you want to ask three or four or more questions.
Sensing, too, is going to be a thing.
You can ask questions aka Boolean expressions like is the sprite touching the mouse pointer, the arrow on the screen?
So that you can start to interact with these programs.
What is the distance between a sprite and a mouse pointer?
You can do simple calculations just to figure out maybe if the enemy is getting close to the cat.
Under Operator some lower level stuff like math, but also the ability to pick random numbers, which for a game is great because then you can kind of vary the difficulty or what's happening in a game without the same game playing the same way every time.
And you can combine ideas.
Something and something must be true in order to make that kind of decision before.
Or we can even join two words together.
Says apple and banana by default, but you can type in or drag and drop whatever you want there to combine multiple words into full, larger sentences.
Then lastly down here, there's in orange things called variables.
In math we've obviously got x and y and whatnot.
In programming we’ll have the same ability to store in these named symbols, x or y, values that we care about.
Numbers or letters or words or colors or anything, ultimately.
But in programming you'll see that it's much more conventional not to just use simple letters like x and y and z, but to actually give variables full singular or plural words to describe what they are.
Then lastly, if this isn’t enough color blocks for you, you can create your own blocks.
Indeed, this is going to be a programming principle we'll apply today and with the first problem set whereby once you start to assemble these puzzle pieces and you realize, oh, would have been nice if those several pieces could have just been replaced by one had MIT thought to give me that one puzzle piece, you yourself can make your own blocks by connecting these all together, giving them a name, and boom, a new puzzle piece will exist.
So let's do the simplest, most canonical programs here, starting up with control, and I'm going to click and drag and drop this thing here when green flag clicked.
Then I'm going to grab one more, for instance under Looks, and under Looks I'm going to go ahead and just say something like initially not just Hello but the more canonical Hello comma world.
Now you might guess that in this programming environment, I can go over here now and click the green flag and voila, Hello comma world.
So that's my first program and obviously much more user friendly than typing out the much more cryptic text that we saw on the screen that you, too, will type out next week.
But for now, we'll just focus on these ideas, in this case, a function.
So what it is that just happened?
This purple block here is Say, that's the function, and it seems to take some form of input in the white oval, specifically Hello comma world.
Well this actually fits the paradigm that we looked at earlier of just inputs and outputs.
So if I may, if you consider what this puzzle piece is doing, it actually fits this model.
The input in this case is going to be Hello comma world in white.
The algorithm is going to be implemented as a function by MIT called Say and the output of that is going to be some kind of side effect, like the cat and the speech bubble are saying Hello, world.
So already even that simple drag and drop mimics exactly this relatively simple mental model.
So let's take things further.
Let's go ahead now and make the program a little more interactive so that it says something like Hello, David, or Hello, Carter, or Hello to you specifically.
And for this, I'm going to go under Sensing.
And you might have to poke around to find these things the first time around, but I've done this a few times so I kind of know where things are and what color.
There's this function here.
Ask what's your name, but that's in white, so we can change the question to anything we want, and it's going to wait for the human to type in their answer.
This function called Ask is a little different from the Say block, which just had this side effect of printing a speech bubble to the screen.
The ask function is even more powerful in that after it asks the human to type something in.
This function is going to hand you back what they typed in in the form of what's called a return value, which is stored ultimately and by default this thing called Answer.
This little blue oval here called Answer is again one of these variables that in math would be called just x or y but in programming we're saying what it does.
So I'm going to go ahead and do this.
Let me go ahead and drag and drop this block and I want to ask the question before saying anything, but you'll notice that Scratch is smart and it's going to realize I want to insert something in between and it's just going to move things up and down.
I'm going to let go and ask the default question, what's your name?
And now if I want to go ahead and say hello, David or Carter, let's just do Hello comma, because I obviously don't know when I'm writing the program who's going to use it.
So let me now grab another looks block up here, say something again, and now let me go back to Sensing and now grab the return value, represented by this other puzzle piece, and let me just drag and drop it here.
Notice it's the same shape, even if it's not quite the same size.
Things will grow or shrink as needed.
All right, so let's now zoom out.
Let me go and stop the old version because I don't want to say Hello, world anymore.
Let me hit the green flag and what's my name? All right, David.
Enter. Huh. All right, maybe I just wasn't paying close enough attention.
Let me try it again. Green flag, D-A-V-I-D, Enter.
This seems like a bug. What's the bug or mistake might you think?
Yeah?

AUDIENCE: Do you need to somehow add them together in the same text box?

DAVID MALAN: Yeah, we kind of want to combine them in the same text box.
And it's technically a bug because this just looks kind of stupid.
It's just saying David after I asked for my name.
I'd like it to say maybe Hello then David, but it's just blowing past the Hello and printing David.
But let's put our finger on why this is happening.
You're right for the solution, but what's the actual fundamental problem?
In back.

AUDIENCE: So it says hello, but it gets to that last step so quickly you can't see it.

DAVID MALAN: Perfect. I mean, computers are really darn fast these days.
It is saying Hello, all of us are just too slow in this room to even see it because it's then saying David on the screen so fast as well.
So there's a couple of solutions here, and yours is spot on, but just to poke around, you'll see the first example of how many ways in programming be it Scratch or C or Python or anything else, that there are going to be to solve problems?
We'll teach you over the course of these weeks, sometimes some ways are better relatively than others, but rarely is there a best way necessarily, because again reasonable people will disagree.
And what we'll try to teach you over the coming weeks is how to kind of think through those nuances.
And it's not going to be obvious at first glance, but the more programs you write, the more feedback you get, the more bugs that you introduce, the more you'll get your footing with exactly this kind of problem solving.
So let me try this in a couple of ways. Up here would be one solution to the problem.
MIT anticipated this kind of issue, especially with first-time programmers, and I could just use a puzzle piece that says say the following for two seconds or one second or whatever, then do the same with the next word and it might be kind of a bit of a pause, Hello, one second, two seconds, David, one second, two seconds, but at least it would look a little more grammatically correct.
But I can do it a little more elegantly, as you've proposed.
Let me go ahead and throw away one of these blocks, and you can just drag and let go and it'll delete itself.
Let me go down to Operators because this Join block here is the right shape.
So even if you're not sure what goes where, just focus on the shapes first.
Let me drag this over here. It grew to fill that. Let me go ahead and say hello comma space.
Now it could just say by default Hello, banana, but let me go back to Sensing, Drag answer, and that's going to drag and drop there.
So now notice we're sort of stacking or nesting one block on another so that the output of one becomes the input to another, but that's OK here.
Let me go ahead and zoom out, hit Stop, and hit Play.
All right, what's your name?
D-A-V-I-D, Enter, and voila. Now it's presumably as we first intended.
[APPLAUSE]
(LAUGHING) Oh, thank you. Thank you. No minus 2 this time.
So consider that even with this additional example, it still fits the same mental model, but in a little more interesting way.
Here's that new function Ask something and wait.
And notice that in this case too there's an input, otherwise known henceforth as an argument or a parameter, programming speak for just an input in the context of a function.
If we use our drawing as before to represent this thing here, we'll see that the input now is going to be quote unquote "What's your name?"
The algorithm is going to be implemented by way of this new puzzle piece, the function called Ask, and the output of that thing this time is not going to be the cat saying anything yet, but rather it's going to be the actual answer.
So instead of the visual side effect of the speech bubble appearing, now nothing visible is happening yet.
Thanks to this function it's sort of handing me back like a scrap of paper with whatever I typed in written on it so I can reuse D-A-V-I-D one or more times even like I did.
Now what did I then do with that value?
Well consider that with the subsequent function we had this Say block, too, combined with a join.
So we have this variable called Answer, we're joining it with that first argument, Hello.
So already we see that some functions like Join can take not one but two arguments, or inputs, and that's fine.
The output of Join is presumably going to be Hello, David or Hello, Carter or whatever the human typed in.
That output notice is essentially becoming the input to another function, Say, just because we've kind of stacked things or nested them on top of one another.
But methodically, it's really the same idea.
The input now are two things, Hello comma and the return value from the previous Ask function.
The function now is going to be Join, the output is going to be Hello, David.
But that Hello, David output is now going to become the input to another function, namely that first block called Say, and that's then going to have the side effect of printing out Hello, David on the screen.
So again as sort of sophisticated as ours as yours as others programs are going to get, they really do fit this very simple mental model of inputs and outputs and you just have to learn to recognize the vocabulary and to know what kinds of puzzle pieces or concepts ultimately to apply.
But you can ultimately really kind of spice these things up.
Let me go back to my program here that just is using the speech bubble at the moment.
Scratch's inside has some pretty fancy interactive features, too.
I click the Extensions button in the bottom left corner.
And let me go ahead and choose the Text to Speech extension.
This is using a Cloud service, so if you have an internet connection it can actually talk to the Cloud or a third party service, and this one is going to give me a few new green puzzle pieces, namely the ability to speak something from my speakers instead of just saying it textually.
So let me go ahead and drag this.
Now notice I don't have to interlock them if I'm just kind of playing around and I want to move some things around.
I just want to use this as like a canvas temporarily.
Let me go ahead and steal the Join from here, put it there, let me throw away the Say block by just moving it left and letting go, and now let me join this in so I've now changed my program to be a little more interesting.
So now let me stop the old version.
Let me start the new.
What's your name? Type in David.
And voila: PROGRAM: Hello, banana.

DAVID MALAN: (LAUGHING) OK, minus 2 for real.
All right, so what I accidentally threw away there, intentionally for instructional purposes, was the actual answer that came back from the ask block.
That's embarrassing.
So now if I play this again, let's click the green icon.
What's your name? David.
And now: PROGRAM: Hello, David.

DAVID MALAN: There we go. Hello, David. All right, thank you.
[APPLAUSE]
OK, so we have these functions then in place, but what more can we do?
Well what about those conditionals and loops and other constructs?
How can we bring these programs to life so it's not just clicking a button and voila, something's happening?
Let's go ahead and make this now even more interactive.
Let me go ahead and throw away most of these pieces and let me just spice things up with some more audio under Sound.
I'm going to go to Play Sound Meow until done.
Here we go, green flag.
[MEOW] OK, it's a little loud, but it did exactly do what it said. Let's hear it again.
[QUIETER MEOW] OK.
It's kind of an underwhelming program eventually since you'd like to think that the cat would just meow on its own, but.
[MEOW] I have to keep hitting the button.
Well this seems like an opportunity for doing something again and again.
So all right, well if I wanted to meow, meow, meow, let me just grab a few of these, or you can even right click or Control click and you can Copy Paste even in code here.
Let me play this now.
[THREE MEOWS]
All right, so now like it's not really emoting happiness in quite the same way.
It might be hungry or upset. So let's slow it down.
Let me go to Control, wait one second in between, which might be a little less worrisome. Here we go, Play.
[THREE SLOWER MEOWS]
OK, so if my goal was to make the cat meow three times, I dare say this code or algorithm is correct. But let's now critique its design. Is this well-designed?
And if not, why not? What are your thoughts here? Yeah?

AUDIENCE: You could use the forever or a repeat to make it more--

DAVID MALAN: Yeah, so yeah, agreed. I could use forever or repeat, but let me push a little harder. But why?
Like this works, I'm kind of done with the assignments, what's bad about it?

AUDIENCE: There's too much repetition.

DAVID MALAN: Yeah, there's too much repetition, right?
If I wanted to change the sound that the cat is making to a different variant of meow or have it bark instead like a dog, I could change it from the dropdown here apparently, but then I'd have to change it here and then I'd have to change it here, and God, if this were even longer that just gets tedious quickly and you're probably increasing the probability that you're going to screw up and you're going to miss one of the dropdowns or something stupid and introduce a bug.
Or, if you wanted to change the number of seconds you're waiting, you've got to change it in two, maybe even more places.
Again, you're just creating risk for yourself and potential bugs in the program.
So I do like the repeat or the forever idea so that I don't repeat myself.
And indeed, what I alluded to being possible, copy pasting earlier, doesn't mean it's a good thing.
And in code, generally speaking, when you start to copy and paste puzzle pieces or text next week, you're probably not doing something quite well.
So let me go ahead and throw away most of these to get rid of the duplication, keeping just two of the blocks that I care about.
Let me grab the Repeat block for now, let me move this inside of the Repeat block, it's going to grow to fit it, let me reconnect all this and change the 10 just to a 3, and now, Play.
[THREE SLOW MEOWS] So, better. It's the same thing.
It's still correct, but now I've set the stage to let the cat meow, for instance, four times by changing one thing, 40 times by changing one thing, or it could just use the Forever block and just walk away and it will meow forever instead.
If that's your goal, that would be better.
A better design but still correct.
But you know what?
Now that I have a program that's designed to have a cat meow, wow like why?
I mean, MIT invented Scratch, Scratch as a cat, why is there no puzzle piece called Meow?
This feels like a missed opportunity.
Now to be fair, they gave us all the building blocks with which we could implement that idea, but a principle of programming and really computer science is to leverage what we're going to now start calling Abstraction.
We have step-by-step instructions here, the Repeat, the Play, and the Wait that collectively implements this idea that we humans would call meowing.
Wouldn't it be nice to abstract away those several puzzle pieces into just one that literally just says what it does, meow?
Well here's where we can make our own blocks.
Let me go over here to Scratch under the pink block category here and let me click Make a Block.
Here I see a slightly different interface where I can choose a name for it and I'm going to call it Meow.
I'm going to keep it simple.
That's it. No inputs to meow yet. I'm just going to click OK. Now I'm just going to clean this up a bit here. Let me drag and drop Play Sound and Wait over here.
And you know what?
I'm just going to drag this way down here, way down here because now that I’m done implementing Meow, I'm going to literally abstract it away, sort of out of sight, out of mind, because now notice at top left there is a new pink puzzle piece called Meow.
So at this point, I'd argue it doesn’t really matter how Meow is implemented.
Frankly, I don't know how Ask or Say was implemented by MIT.
They abstracted those things away for us. Now I have a brand new puzzle piece that just says what it is. And this is now still correct, but arguably better design.
Why?
Because it's just more readable to me, to you, it's more maintainable when you look at your code a year from now for the first time because you're sort of finally looking back at the very first program you wrote.
It says what it does.
The function itself has semantics, which conveys what's going on.
If you really care about how Meow is implemented, you could scroll down and start to tinker with the underlying implementation details, but otherwise you don't need to care anymore.
Now I feel like there's an even additional opportunity here for abstraction and to factor out some of this functionality.
It's kind of lame that I have this Repeat block that lets me call the Meow function, so to speak, use the Meow function three times.
Wouldn't it be nice if I could just call them Meow function, aka use the Meow function, and pass it in input that tells the puzzle piece how many times I want it to meow?
Well let me go ahead and zoom out and scroll down.
Let me right click or Control click on the pink piece here and choose Edit, or I could just start from scratch, no pun intended, with a new one.
Now here, rather than just give this thing a name Meow, let me go ahead and add an input here.
I'm going to go ahead and type in, for instance, n, for number of times to meow, and just to make this even more user friendly and self descriptive, I'm going to add a label, which has no functional impact, it's just an aesthetic, and I'm just going to say Times, just to make it read more like English in this case that tells me what the puzzle piece does.
Now I'm going to click OK. And now I need to refine this a little bit.
Let me go ahead and grab under Control a repeat block, let me move the Play, Sound, and Wait, into the repeat block.
I don't want 10 and I also don't want 3 here.
What I want now is this n that is my actual variable that Scratch is creating for me that represents whatever input the human programmer provides.
Notice that snaps right in place.
Let me connect this and now voila, I have an even fancier version of Meow that is parameterized.
It takes input that affects its behavior accordingly.
Now I'm going to scroll back up, because out of sight, out of mind, I just care that Meow exists.
Now I can tighten up my code, so to speak, use even fewer lines to do the same thing by throwing away the Repeat block, reconnecting this new puzzle piece here that takes an input like 3 and voila, now we're really programming, right?
We've not made any forward progress functionally. The thing just mouse three times. But it's a better design.
As you program more and more, these are the kinds of instincts still start to acquire so that one, you can start to take a big assignment, a big problem set, something for homework even, that feels kind of overwhelming at first, like, oh my God where do I even begin?
But if you start to identify what are the subproblems of a bigger problem?
Then you can start making progress.
I do this to this day where if I have to tackle some programming-related project it's so easy to drag my feet and ugh, it's going to take forever to start, until I just start writing down like a to do list and I start to modularize the program and say, all right, well what do I want this thing to do?
Meowing. What's that mean? I've got to have it say something on the screen.
All right, I need to have it say something on the screen some number of times.
Like literally a mental or written checklist, or pseudocode code, if you will, in English on a piece of paper or text file, and then you can decide, OK, the first thing I need to do for homework to solve this real world problem, I just need a Meow function.
I need to use a bunch of other code, too, but I need to create a Meow function and boom, now you have a piece of the problem solved not unlike we did with the phone book there, but in this case, we’ll have presumably other problems to solve.
All right, so what more can we do? Let's add a few more pieces to the puzzle here. Let's actually interact with the cat now.
Let me go ahead and now when the green flag is clicked, let me go ahead and ask a question using an event here.
Let me go ahead and say, let's see, I want to do something like implement the notion of petting the cat.
So if the cursor is touching the cat like here, something like this, it'd be cute if the cat meows like you're petting a cat.
So I'm going to ask the question, when the green flag is clicked, if let's see I think I need Sensing.
So if touching mouse pointer, this is way too big but again the shape is fine, so there goes. Grew to fill.
And then if it's touching the mouse pointer, that is if the cat to whom this script or this program, any time I attach puzzle pieces MIT calls them a script or like a program, if you will, let me go ahead then and choose a sound and say play sound meow until done.
All right, so here it is to be clear.
When the green flag is clicked, ask the question, if the cat is touching the mouse pointer then place sound meow.
Here we go. Play.
[SILENCE] All right, let's try again. Play.
[SILENCE] Huh. I'm worried it's not Scratch's fault. Feels like mine.
What's the bug here? Why doesn't this work? Yeah, in back, who just turned.

AUDIENCE: [INAUDIBLE]

DAVID MALAN: Yeah, the problem is the moment I click that green flag, Scratch asks the question, is the cat touching the mouse pointer?
And obviously it's not because the cursor was like up there a moment ago and it's not down there.
It's fine if I move the cursor down there, but too late.
The program already asked the question.
The answer was no or false or zero, however you want to think about it, so no sound was played.
So what might be the solution here be? I could move my cursor quickly, but that feels like never going to work out right.
Other solutions here? Yeah, in way back?
Could you use the forever loop? The Forever loop.
So I could indeed use this Forever loop because if I want my program to just constantly listen to me, well let's literally do something forever, or at least forever as long as the program is running until I explicitly hit Stop.
So let me grab that.
Let me go to Control, let me grab the Forever block,let me move the If inside of this Forever block, reconnect this, go back up here, click the green flag, and now nothing's happened yet, but let me try moving my cursor now.
[MEOW] Oh. So now.
[MEOW] That's kind of cute.
So now the cat is actually responding and it’s going to keep doing this again and again.
So now we have this idea of taking these different ideas, these different puzzle pieces, assembling them into something more complicated.
I could definitely put a name to this.
I could create a custom block, but for now let's just consider what kind of more interactivity we can do.
Let me go ahead and do this.
By again grabbing a, when green flag clicked, let me go ahead and click the video sensing, and I'm going to rotate the laptop because otherwise we’re going to get a little inception thing here where the camera is picking up the camera is up there.
So I'm going to go reveal to you what's inside the lectern here while we rotate this.
Now that we have a non video backdrop, I'm going to say this.
Instead of the green flag clicked, actually, I’m going to say when the video motion is greater than some arbitrary measurement of motion, I'm going to go ahead and play sound meow until done.
And then I'm going to get out of the way.
So here's the cat. We'll put them on top of there.
[MEOW] OK. All right, and here we go.
[MEOW] So my hand is moving faster than 50 something or other, whatever the unit of measure is.
[MEOW]

AUDIENCE: Aw.

DAVID MALAN: (LAUGHING) Thank you.
So now we have an even more interactive version.
[MEOW] But I think if I sort of slowly.
[LAUGHING]
(LAUGHING) Right?
It's completely creepy, but I’m not like exceeding the threshold--
[MEOW] Until finally my hand moves as fast as that.
And so here actually is an opportunity to show you something a former student did.
Let me go ahead here and--
[MEOW TWICE] OK, got to stop this.
Let me go ahead and zoom out of this in just a moment.
[MEOW] If someone would be--
[LAUGHING]
(LAUGHING) If someone would be comfortable coming up not only masked but also on camera on the internet I thought we'd play one of your former classmate's projects here up on stage.
Would anyone like to volunteer here and be up on stage?
Who's that? Yeah. Come on down. What's your name?

AUDIENCE: Sahar.

DAVID MALAN: Sahar. All right, come on down. Let me get it set up for you here.
[MEOW] [APPLAUSE] [MEOW]
All right, let me go ahead and full screen this here.
So this is whack-a-mole by one of your firmer predecessors.
It's going to use the camera focusing on your head, which will have to position inside of this rectangle.
Have you ever played the whack-a-mole game at an arcade?

AUDIENCE: Yeah.

DAVID MALAN: OK.
So for those who haven’t, these little moles pop up and with a very fuzzy hammer you sort of hit down.
You though, if you don't mind, you're going to use your head to do this virtually.
So let's line up your head with this red rectangle, if you could, we'll do beginner.
[MUSIC PLAYING] All right, here we go. Sahar. Give it a moment.
OK, come a little closer.
[DINGING] And now hit the moles with your head.
[DING] There we go, one point.
[DING] One point.
[DINGING] Nice. 15 seconds to go. There we go. Oh yeah. One point.
[LAUGHING] [DINGING] Six seconds.

AUDIENCE: Oh no.

DAVID MALAN: There we go. Quick!
[DINGING] All right, a round of applause for Sahar. Thank you.
[APPLAUSE]
So beyond having a little bit of fun here, the goal was to demonstrate that by using some fairly simple, primitive, some basic building blocks but assembling them in a fun way with some music, maybe some new costumes or artwork, you can really bring programs to life.
But at the end of the day, the only puzzle pieces really involved were ones like the ones I just dragged and dropped and a few more, because there were clearly lots of moles.
So the student probably created a few different sprites, not a single cap, but at least four different moles.
They had like some kind of graphic on the screen that showed Sahar where to position her head.
There were some kind of timer, maybe a variable that every second was counting down.
So you can imagine taking what looks like a pretty impressive project at first glance, and perhaps overwhelming to solve yourself, but just think about what are the basic building blocks?
And pluck off one piece of the puzzle, so to speak, at a time.
So indeed if we rewind a little bit.
Let me go ahead here and introduce a program that I myself made back in graduate school when Scratch was first being developed by MIT.
Let me go ahead and open here, give me just one second, something that I called back in the day Oscar Time that looks a little something like this.
If I fullscreen it and hit Play.
[MUSIC - SESAME STREET, "I LOVE TRASH"]
OSCAR THE GROUCH: (SINGING) Oh, I love trash.

DAVID MALAN: So you'll notice a piece of trash is falling.
I can click on it and drag and as I get close and close to the trash can notice OSCAR THE GROUCH: (SINGING) Anything ragged or--

DAVID MALAN: It wants to go in, it seems.
And if I let go--
OSCAR THE GROUCH: (SINGING) Yes, I--

DAVID MALAN: One point.
Here comes another.
OSCAR THE GROUCH: (SINGING) If you really want to see something trashy--

DAVID MALAN: I'll do the same, two points.
OSCAR THE GROUCH: (SINGING) I have here a sneaker that's tattered and worn--

DAVID MALAN: There's a sneaker falling from the sky, so another sprite of some sort.
OSCAR THE GROUCH: (SINGING) The laces are torn.
A gift from my mother--

DAVID MALAN: I can also get just a little lazy and just let them fall into the trash themself if I want to.
So you can see it doesn't have to do with my mouse cursor, it has to do apparently with the distance here.
Let's listen a little further. I think some additional trash is about to make its appearance. Presumably there's some kind of variable that's keeping track of this score.
OSCAR THE GROUCH: (SINGING) I love--

DAVID MALAN: OK, let's see what the last chorus here is.
OSCAR THE GROUCH: (SINGING) Rotten stuff.
I have here some newspaper, crusty and
DAVID MALAN: OK, and thus he continues.
And the song actually goes on and on and on and I do not have fond memories of implementing this and hearing this song for like 10 straight hours, but it's a good example to just consider how was this program composed?
How did I go about implementing it the first time around?
And let me go ahead and open up some programs now that I wrote in advance just so that we could see how these things are assembled.
Honestly, the first thing I probably did was probably to do something a little like this.
Here is just a version of the program where I set out to solve just one problem first of planting a lamp post in the program.
Right? I kind of had a vision of what I wanted.
You know, it evolved over time, certainly, but I knew I wanted trash to fall, I wanted a cute little Oscar the Grouch to pop out of the trashcan, and some other stuff, but wow that's a lot to just tackle all at once.
I'm going to start easy, download a picture of a lamp post, and then drag and drop it into the stage as a costume and boom, that's version one.
It doesn't functionally do anything. I mean, literally that's the code that I wrote to do this.
All I did was use like the Backdrops feature and drag and drop and move things around, but it got me to version one of my program.
Then what might version two be?
Well I considered what piece of functionality frankly might be the easiest to pluck off next and the trash can.
That seems like a pretty core piece of functionality. It just needs to sit there most of the time.
So the next thing I probably did was to open up, for instance, the trash can version here that looks a little something now like this.
So this time I'll show you what's inside here. There is some code, but not much.
Notice at bottom right I change the default cat to a picture of a trashcan, instead, but it's the same principle that I can control.
And then over here I added this code.
When the green flag is clicked, switch the costume to something I arbitrarily called Oscar 1.
So I found a couple of different pictures of a trash can, one that looks closed, one that looks partly open, and eventually one that has Oscar coming out, and I just gave them different names.
So I said Switch to Oscar 1, which is the closed one by default, then forever do the following: if touching the mouse pointer, then switch the costume to Oscar 2, else switch to Oscar 1.
That is to say, I just wanted to implement this idea of the can opening and closing, even if it's not exactly what I wanted ultimately, I just wanted to make some forward progress.
So here, when I run this program by clicking Play, notice what happens.
Nothing yet, but if I get closer to the trash can, it indeed pops open because it's forever listening for whether the sprite, the trash can in this case, is touching the mouse pointer.
And that's it.
That was version 2, if you will.
If I went in now and added the lamp post and compose the program together, now we're starting to make progress.
Right?
Now it would look a little something more like the program I intended ultimately to create.
What piece did I probably bite off after that?
Well, I think what I did is I probably decided let me implement one of the pieces of trash, not the shoe in the newspaper all at once.
Let's just get one piece of trash working correctly first.
So let me go ahead and open this one.
And again, all of these examples will be available on the course's website so you can see all of these examples, too.
It's not terribly long, I just implement it in advance so we could flip through kind of quickly.
Here's what I did here.
On the right hand side, I turned my sprite into a piece of trash this time instead of a cat, instead of a trash can, and I also created, with Carter's help, a second sprite, this one a floor.
It's literally just a black line because I just wanted initially to have some notion of a floor so I could detect if the trash is touching the floor.
Now without seeing the code yet, just hearing that description, why might I have wanted the second sprite and this black line for a floor with the trash intending to fall from the sky?
What might I have been thinking?
Like what problem might I be trying to solve?
Yeah?

AUDIENCE: You don't want the first sprite to go through it.

DAVID MALAN: Yeah, you don't want the first sprite to start at the top, go through, and then boom, you completely lose it.
That would not be a very useful thing.
Or it would seem to maybe eat up more and more of the computer's memory if the trash is just endlessly falling and I can't grab it.
It might be a little traumatic if you tried to get it and you can't pull it back out and you can't fix the program.
So I just wanted the thing to stop.
So how might I have implemented this?
Let's look at the code at left.
Here I have a bit of randomness, like I proposed earlier exists.
There's this blue function called Go To x, y that lets me move a sprite to any position, up, down, left, right, I picked a random x location, either here or over here, negative 240 to positive 240, and then a y value of 180, which is the top.
This just makes the game more interesting.
It's kind of lame pretty quickly if the trash always falls from the same spot.
Here's this a little bit of randomness, like most any game would have, that spices things up.
So now if I click the green flag, you'll see that it just falls, nothing interesting is going to happen, but it does stop when it touches the black line because notice what we did here.
I'm forever asking the question if the distance of the sprite, the trash, is to the floor is greater than zero, that's fine.
Change the y location by negative 3.
So move it down 3 pixels, down 3 pixels, until the distance to the floor is not greater than zero, it is zero or even negative, at which point it should just stop moving altogether.
There's other ways we could have implemented this, but this felt like a nice, clean way that logically, just made it make sense.
OK, now I got some trash falling, I got a trash can that opens and closes, I have a lamp post, now I'm a good three steps into the program.
We're making progress.
If we consider one or two final pieces, something like the dragging of the trash, let me go ahead and open up this version 2.
Dragging the trash requires a different type of question.
Let me zoom in here.
Here's the piece of trash.
I only need one sprite, no floor here because I just want the human to move it up, down, left, right and the human's not going to physically be able to move it outside of the world.
If we zoom in on this code, the way we've solved this is as follows.
We're using that And conjunction that we glimpsed earlier because when the green flag is clicked, we're forever asking this question or really these questions, plural, if the mouse is down and the trash is touching the mouse pointer, that's equivalent logically to clicking on the trash.
Go ahead and move the trash to the mouse pointer.
So again it takes this very familiar idea that you and I take for granted every day on Macs and PCs of clicking and dragging and dropping.
How is that implemented?
Well Mac OS or Windows are probably asking a question.
For every icon, is the mouse down and is the icon touching the mouse?
If so, go to the location of the mouse forever while the mouse button is clicked down.
So how does this work in reality now?
Let me go ahead and click on the Play.
Nothing happens at first, but if I click on it, I can move it up, down, left, right.
It doesn't move thereafter.
So I now need to kind of combine this idea of dragging with falling, but I bet I could just start to use just one single program.
Right now I'm using separate ones to show different ideas, but now that's another bite out of the problem.
If we do one last one, something like the scorekeeping is interesting, because recall that every time we dragged a piece of trash into the can, Oscar popped out and told us the current score.
So let me go ahead and find this one, Oscar variables, and let me zoom in on this one.
This one is longer because we combined all of these elements.
So this is the kind of thing that if you looked at first glance, like, I have no idea how I would have implemented this from nothing, from scratch literally.
But again, if you take your vision and componenitize it into these smaller, bite-sized problems, you could take these baby steps, so to speak, and then solve everything collectively.
So what's new here is this bottom one.
Forever do the following: if the trash is touching Oscar, the other sprite that we've now added to the program, change the score by 1.
This is an orange and indeed if we poke around we'll see that orange is a variable, like an x or y but with a better name, changing it means to add 1 or if it's negative subtract 1.
Then go ahead and have the trash go to pick random.
What is this all about?
Well, let me show you what it's doing and then we can infer backwards. Let me go ahead and hit Play.
All right, it's falling, I'm clicking and dragging it, I'm moving it over, and I'm letting go. All right, let me do it once more.
Letting go, let me stop.
Why do I have this function at the end called Go To x and y randomly?
Like what problem is this solving here? Yeah, in way back.

AUDIENCE: Just the same track teleported to the top after you put it in the trash can.

DAVID MALAN: Yeah, exactly.
Even though the human perceives this as like a lot of trash falling from the sky, it's actually the same piece of trash, just kind of being magically moved back to the top as though it's a new one.
There, too, you have this idea of reusable code.
If you were constantly copying and pasting your pieces of trash and creating 20 pieces of trash, 30 pieces of trash, just because you want the game to have that many levels, probably doing something wrong.
Reuse the code that you wrote, reuse the sprites that you wrote, and that would give you not just correctness, but also a better design.
Well let's take a look at one final set of building blocks that we can compose ultimately into something particularly interactive as follows.
Let me go ahead and zoom out here and let me propose that we implement something like some kind of maze-based game.
Let me go ahead here.
So I want to implement some maze-based game that looks at first glance like this.
Let me hit Play.
It's not a very fun game yet, but here's a little Harvard shield, a couple of black lines, this time vertical instead of horizontal, but notice you can't quite see my hand here, but I'm using my arrow keys to go down, to go up, to go left, to go right, but if I keep going right, right, right, right, right, right, right it's not going anywhere.
And left, left, left, left, left, left, left, left, left, left, left, left, left it eventually stops.
So before we look at the code, how might this be working?
What kinds of scripts, collections of puzzle pieces, might collectively help us implement this?
What do you think?

AUDIENCE: [INAUDIBLE]

DAVID MALAN: Perfect, yeah.
There's probably some question being asked, if touching the black line, and it happens to be a couple of sprites, each of which is just literally a vertical black line we're probably asking a question like, are you touching it?
Is the distance to it zero or close to zero?
And if so, we just ignore the left or the right arrow at that point.
So that works.
But otherwise, if we're not touching a wall, what are we probably doing instead forever here?
How is the movement working presumably?
Yeah and back. Oh are you scratching? OK, sure. Let's go on.

AUDIENCE: [INAUDIBLE]

DAVID MALAN: Sorry, say a little louder.

AUDIENCE: Presumably it's continually looking for you to hit the arrow keys and then moving when you do.

DAVID MALAN: Exactly.
It's continually, forever listening for the arrow keys up, down, left, right, and if the up arrow is pressed, we're probably changing the y by a positive value.
If the down arrow is pressed, we're going down by y, and left and right accordingly.
So let's actually take a quick look.
If I zoom out here and take a look at the code that implements this, there's a lot going on at first glance, but let's see.
First of all, let me drag some stuff out of the way because it's kind of overwhelming at first glance, especially if you, for instance, were poking around online as for problem set 0 just to get inspiration, most projects out there are going to look overwhelming at first glance until you start to wrap your mind around what's going on.
But in this case, we've implemented some abstractions from the get go to explain to ourselves and to anyone else looking at the code what's going on.
This is that program with the two black lines and the Harvard shield going up, down, left, and right.
It initially puts the shield in the middle, 0,0, then forever listens for keyboard, as I think you were describing, and it feels for the walls, as I think you were describing.
Now how is that implemented?
Don't know yet.
These are custom blocks we created as abstractions to kind of hide those implementation details because honestly that's all I need to know right now.
But, as aspiring programmers, if we're curious now, let's scroll down to the actual implementation of listening for keyboard.
This is the one on the left and it is a little long, but it's a lot of similar structure.
We're doing the following, if the up arrow is pressed, then change y by 1.
Go up. If the down arrow is pressed, then change y by negative 1. Go down.
Right arrow, left arrow, and that's it.
So it just assembles all of those ideas, combines it into one new block just because it's kind of overwhelming, let's just implement it once and tuck it away.
And if we scroll now over to the Feel for Walls function, this now is asking the question as hypothesized, if I'm touching the left wall, change my x value by 1, sort of move away from it a little bit.
If I'm touching the right wall, then move x by negative 1 to move a little bit away from it.
So it kind of bounces off the wall.
Just in case it slightly went over, we keep the crest within those two walls.
All right, then a couple of more pieces here to introduce.
What if we want to actually add some kind of adversary or opponent to this game?
Well, let me go ahead to maybe this one here where the adversary in this game might, for instance, be designed to be bouncing to stand in your way.
This is like a maze and you're trying to get the Harvard shield from the bottom to the top or vice versa.
Uh oh, Yale is in the way and it seems to be automatically bouncing back and forth here.
Well, let me ask someone else. Hypothesize. How is this working?
This is an idea you have, this as an idea you see. Let's reverse engineer in your head how it works. How might this be working?
Yeah, in back.

AUDIENCE: If the Yale symbol is touching a right wall or left wall, then have it bounce.

DAVID MALAN: Yeah, so if the Yale symbol is touching the left wall or the right wall, we somehow have it bounce.
And indeed we'll see there's a puzzle piece that can do exactly that technically off the edge, as we'll see, but there's another way we can do this.
Let's look at the code.
The way we ourselves can implement exactly that idea bounce is just with a little bit of logic.
So here's what this version of the program is doing.
It's moving Yale by default to 0,0 just to arbitrarily put it somewhere, pointing it direction 90 degrees, which means just horizontally, essentially, and then it's forever doing this: if touching the left wall or touching the right wall,here's our translation of bounce.
We're just turning 180 degrees.
And the nice thing about that is we don’t have to worry if we're going from right to left or left to right.
180 degrees is going to work on both of the walls.
And that's it.
After we do that, we just move one step, one pixel, at a time but we're doing it forever so something is happening continually and the Yale icon is bouncing back and forth.
Well one final piece here, what if now we want another adversary, a more advanced adversary down the road for instance, to go and follow us wherever we are such that this time we want the other sprite to not just bounce back and forth, but literally follow us no matter where we go.
How might this be implemented on the screen?
I bet it's another forever block, but what's inside?

AUDIENCE: So forever get the location of the of the Harvard shield and move one step towards it.

DAVID MALAN: Yeah, forever point at the location of the Harvard shield and go one step toward it.
This is just going to go on forever if I just give up, at least in this version.
Notice it's sort of twitching back and forth because it goes one pixel then one pixel then one pixel.
It's sort of in a frantic state here.
We haven't finished the game yet, but if we see inside, we'll see exactly that.
It didn't take much to implement this simple idea.
Go to a random position just to make it kind of fair, initially, then forever point towards Harvard, which is what we called the Harvard crest sprite, move one step.
Suppose we now wanted to make a more advanced level.
What's a minor change I could logically make to this code just to make MIT even better at this?

AUDIENCE: Change the number of steps to two.

DAVID MALAN: All right, change the number of steps to two.
So let's try that.
So now they got twice as fast.
Let me go ahead and just get this out of the way.
Oops, let me make it a fair fight.
Green flag.
All right, I unfortunately am still moving one pixel at a time, so this isn't going to end well.
It caught up to me.
And if we're really aggressive and do something like 20 steps at a time, click the green flag.
Jesus, OK, so that's how you might then make your levels progressively harder and harder.
So it's not an accident that we chose these particular examples here involving these particular schools because we have one more demonstration we thought we'd introduce today if we could get one other volunteer to come up and play what was called by one of your predecessors Ivy's Hardest Game.
Let's see, you in the middle.
Do you want to come on up?
What's your name?

AUDIENCE: Celeste.

DAVID MALAN: Say again?

AUDIENCE: Celeste.

DAVID MALAN: Come a little closer, actually.
Sorry, hard to hear here.
All right, round of applause here if we could, too.
[APPLAUSE]
OK, sorry, what was your name?

AUDIENCE: Celeste.

DAVID MALAN: Ceweste.

AUDIENCE: Celeste.

DAVID MALAN: Celeste.

AUDIENCE: Yes.

DAVID MALAN: Come on over.
Nice to meet you, too.
So here we have on this other screen Ivy's Hardest Game written by a former CS50 student.
I think you'll see that it combines these same principles.
The maze is clearly a little more advanced.
The goal at hand is to initially move the Harvard crest to the sprite all the way on the right so that you catch up to him in this case, but you'll see that there's different levels and different levels of sophistication.
So if you're up for it, you can use just these arrow keys up, down, left, right.
You'll be controlling the Harvard sprite and if we could raise the volume just a little bit, we'll make this our final example.
Here we go, clicking the green flag.
[MUSIC PLAYING]
Feeling ready?

AUDIENCE: Yep.

DAVID MALAN: Spacebar.
[MUSIC - MC HAMMER, "U CAN'T TOUCH THIS"]
MC HAMMER: (SINGING) Can't touch this.
You can't touch this.
You can't touch this.
Can't touch this.
My, my, my, my music--

DAVID MALAN: Excellent.
MC HAMMER: (SINGING) so hard.
Makes me want to say, oh my Lord.
Thank you for blessing me--

DAVID MALAN: Two Yales now.
MC HAMMER: (SINGING) Feels good when you know you're down.
A super dope homeboy--

AUDIENCE: Oh!

DAVID MALAN: Oh! Keep going.
MC HAMMER: (SINGING) You can't touch this. I told you, homeboy. Can't touch this.
Yeah, that's how living--

DAVID MALAN: All right.
MC HAMMER: (SINGING) Can't touch this.
Look at my eyes, man. You can't touch this. You let me bust the funky lyrics.
You can't touch this. Fresh new kicks and pants. You got it like that and you know you want to dance. So move out of your seat and get a fly girl and catch this beat.
[LAUGHING] Hold on.
Pump a little bit and let them know what's going on like that, like that.
Cold on a mission, so fall on back. Let them know that you're too--

DAVID MALAN: There you go. There you go.
[APPLAUSE]
MC HAMMER: (SINGING) Can't touch this.
Why you standing there, man?
You can't touch this. Yo, sound the bell. School's in, sucker. Can't touch this.
Give me a song or rhythm, making them sweat that's what give them.
[CHEERING]
They know.
You talking the Hammer when you're talking about a show.
That's hyped and tight.
Singers are sweating so them a wipe or a tame to learn.

DAVID MALAN: Second to last level. Oh!
MC HAMMER: (SINGING) That chart's legit.
Either work hard or you might as well quit.
That word because you know--

DAVID MALAN: Oh!
Keep going, keep going! Yes!
MC HAMMER: (SINGING) You can't touch this.

DAVID MALAN: You're almost there.
MC HAMMER: (SINGING) Break it down.

DAVID MALAN: There you go.
Go, go, go! Oh. One more. Yes!
[CHEERING] There you go.
MC HAMMER: (SINGING) Stop, Hammer time.
"Go with the flow," it is said.
If you can't groove to this, then you're probably dead.
So wave your hands in the air, bust a few moves, run your fingers through your hair.
This is it. For a winner. Dance to this and you’re going to get thinner.
Now move, slide your rump. Just for a minute let's all do the bump.
[CHEERING]

DAVID MALAN: Yes!
[APPLAUSE]
Congratulations. All right, that's it for CS50. Welcome to the class. We'll see you next time.
[MUSIC PLAYING]
