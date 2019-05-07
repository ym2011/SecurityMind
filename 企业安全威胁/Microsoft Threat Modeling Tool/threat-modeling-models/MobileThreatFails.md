##1. Not threat modeling at all

The biggest mistake organizations make with mobile threat modeling is simply failing to do it.

“With everyone I’ve ever worked with outside of Microsoft, no one’s done it until we’ve done it with them and taught them how to do it, threat models just don't exist that much” says Michael Howard, senior principal cybersecurity architect at Microsoft. “Threat models just don’t really exist that much.”

That jibes with recent research. A Ponemon study found that 40 percent of companies don’t scan the code in their mobile apps for security vulnerabilities and 33 percent never even test their apps to ensure they’re secure before releasing them.

Many people don’t model for threats because they don’t realize they can do it, Howard says. Others mistakenly think they can wing it. “Unfortunately, when you do it that way, 99 times out of 100 you get at least something wrong,” he says.

Another deterrent is the intricacy of the process. “The complexity lies in the fact that a proper threat model relies on clear design documentation and a full understanding of how the application has been implemented,” says Steve Manzuik, director of security research at Duo Security. “In a fast-paced [mobile development] environment, this documentation—and even an understanding of the application—does not always exist.”

Solution: Just do it. Threat modeling is a learned skill. The OWASP mobile security project threat model provides a great starting point, with an overview of best practices and methodologies such as STRIDE and DREAD. Familiarize yourself with them and build them into your software development life cycle.

###2. Not using strong authentication

Many developers equate security with encryption and protecting data from disclosure. But that’s only one part of it. Without strong mobile user authentication, data can still end up in the wrong hands.

Unfortunately, many developers misunderstand the authentication process and inadvertently leave the end user open to spoofing attacks.

“They think authentication is about authenticating you or I,” Howard says. “It’s not. It’s also when you’re going to www.bank.com, how do you know you’re at Bank.com and not Baghdad Bob’s Bank? That authentication step has to happen. It’s not just about the bank authenticating you. It’s also about you authenticating the bank. Who are you doing the transaction against? A lot of people really miss that.”

Solution: In addition to encryption, your threat model should include user authentication that requires each party to prove its identity to the other. This is particularly critical if the data your app transmits is subject to regulatory compliance, such as HIPAA. While no security measure is foolproof, authentication reduces the risk of data being compromised more than encryption alone.

#3. Not accounting for encryption keys

Software encryption is critical for protecting the data used by your app. But that encryption is worthless if the keys that unlock it can be stolen because they’re inadequately protected.

“You have to show those keys in the threat model because you want to know what defenses are on the keys,” Howard says. “And people forget that as well. [Either] they don’t have the keys in the threat model, or they do have the keys in the threat model but their defenses are really bad.”

Solution: Make sure you’re using state-of-the-art encryption. Account for the encryption keys in your threat model, including how long the keys are and how they’re secured.

#4. Not using appropriate permissions

As an app becomes more sophisticated, it often requires deeper permissions to carry out tasks it can’t perform on its own. But often these enhanced permissions expose users to increased security risks, so they should never be considered lightly.

“One thing we do see a lot is people building apps with inappropriate permissions,” Howard says. “Let’s pick something really dumb: an expense reporting tool. That thing doesn’t need to read your media library or read your photos, right? It’s an expense reporting app. [But] that’s a big mistake people make—they opt in for more capabilities than the app really needs.”

While all permissions expose data to some level of risk, certain ones, such as location and account-related permissions, can have serious consequences if the associated data falls into the wrong hands.

Solution: Be judicious. Decide what permissions your app needs and avoid asking for access to features, data, or services that aren't actually necessary.

#5. Not securing network communications

Thanks to mobile carrier data caps and the ubiquity of “free Wi-Fi,” it’s expected that mobile devices will be used on unprotected networks. Using SSL/TLS to encrypt the data in transit is a common way to mitigate this. But developers often overlook vulnerabilities that can still leave communications open to a man-in-the-middle attack.

“For example, if you’re using SSL or TLS as a mitigation, then I also want to be sure that the cipher suites that are being used are appropriate,” Howard says. “Because things have changed over the last decade—and we know that SSL2 is completely busted, SSL3 is basically busted, and current versions of TLS have some weaknesses—you really should be using TLS1 with cypher suites that support Perfect Forward Secrecy.”

Solution: Before you release your mobile app, run through a series of “coffee-shop Wi-Fi” attacks, trying to intercept encrypted communications and verifying that certificate pinning is enabled and cipher suites in use are strong.

A model for strong mobile security

No mobile app threat model is perfect, and there will always be more to uncover or fix. But by focusing on the most common threats to your app and staying aware of these common pitfalls, you’ll gain a better understanding of your app, minimize the most egregious risks, and strengthen your security posture.
