troyeSivan = {'for him', 'strawberries and cigarettes', 'lucky strike'}
sashaSloan = {'dancing with your ghost', 'older', 'smiling when i die'}
conanGray = {'greek gods', 'the cut that always bleeds', 'grow'}
madisonBeer = {'selfish'}

print("Welcome to 3:24 AM Tunes. This playlist consists of some of my favourite songs. It will recommend songs based on the vibes, and artist.")
choice = str(input("What's your favourite song? "))

if choice.lower() in troyeSivan:
        print("The song is sang by Troye Sivan. Songs you may like are " + str(troyeSivan) + ".")
elif choice.lower() in sashaSloan:
        print("The song is sang by Sasha Sloan. Songs you may like are " + str(sashaSloan) + ".")
elif choice.lower() in conanGray:
        print("The song is sang by conan gray. Songs you may like are " + str(conanGray) + ".")
elif choice.lower() in madisonBeer:
        print("The song is sang by Madison Beer. This is the only song by Madison Beer in the collection.")
else:
        print("This song is not part of the playlist.")