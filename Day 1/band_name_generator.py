def band_name_generator(nickname, location, year):
    generated_band_name = str(nickname) + " of " + \
        str(location) + " " + "est." + str(year)
    return generated_band_name


location = input(f"Where are you located: ")
year = input(f"What is the founding year: ")
nickname = input(f"Provide a nickname: ")

generated_band_name = band_name_generator(
    nickname=nickname, location=location, year=year)

print("Your band name is ", generated_band_name)
