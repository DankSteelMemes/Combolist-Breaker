import re
import time

high = 32  # Password max length
low = 6    # Password min length

user = ''
sep = ''
pw = ''
outputCount = 0
removedCount = 0
colonCount = 0
semicolonCount = 0
spaceCount = 0
tabCount = 0
elseCount = 0
runCount = 0
runTotal = 0
exceptionCount = 0
hashCount = 0
emailCount = 0
csvCount = 0
startTime = time.time()


def strip_text(data, sepr=None):
    data = data.rstrip('\n')
    data = data.strip(sepr)
    return data


def wrapped_pw(password):
    return bool(re.match(wrapped_regex, password))


wrapped_regex = re.compile('"[^"]*"')
hex_regex = re.compile('[$HEX[]')
email_regex = re.compile("[^@\s]+@[^@\s]+\.[^@.\s]+")
# ([\w.]+)\@(\w+\.\w+)(\.\w+)?
# Another option I tried.

def is_hex(hex):
    return bool(re.match(hex_regex, hex))


def valid_email(email):
        return bool(re.match(email_regex, email))


outfile = open("combolist_output.txt", "w", encoding='utf-8', errors='strict')


with open("C:/pypy3/combolist.txt", "r", encoding='latin-1', errors='strict') as infile:
    for line in infile:
        runCount += 1
        if runCount % 10000000 == 0:
            print('Processed ' + str(runCount / 10000000 * 10) + ' million lines in '
                  + str(int(time.time() - startTime)) + ' seconds')
        try:
            if len(line) < 80 and is_hex(line) is False:
                                # Try to avoid hashes and other junk like csv
                                # around 50 should do for default settings but
                                # go higher if you want to capture longer passwords.
                                # Example: "freddy.tester@yahoo.com" is 23 chars long
                                # if you set the max length to 50 that should let you
                                # grab a password that is up to about 24 chars. There
                                # are other chars that are stripped from the line like
                                # the separator and quotes.
                user, sep, pw = line.partition(":")
                pw = strip_text(pw)
                if len(pw) <= high and len(pw) >= low and sep == ':':
                    if valid_email(pw):
                        user, sep, pw = pw.partition(":")
                        pw = strip_text(pw)
                        if valid_email(pw):
                            user, sep, pw = pw.partition(":")
                            pw = strip_text(pw)
                            if valid_email(pw):
                                colonCount += 1
                                continue
                            else:
                                if wrapped_pw(pw):
                                    strip_text(pw, '"')
                                outputCount += 1
                                outfile.write(pw + '\n')
                                continue
                        else:
                            if wrapped_pw(pw):
                                strip_text(pw, '"')
                            outputCount += 1
                            outfile.write(pw + '\n')
                            continue
                    else:
                        if wrapped_pw(pw):
                            strip_text(pw, '"')
                        outputCount += 1
                        outfile.write(pw + '\n')
                        continue

                else:
                    user, sep, pw = line.partition(" ")
                    pw = strip_text(pw)
                    if len(pw) <= high and len(pw) >= low and sep == ' ':
                        if valid_email(pw):
                            spaceCount += 1
                            continue
                        else:
                            if wrapped_pw(pw):
                                strip_text(pw, '"')
                            outputCount += 1
                            outfile.write(pw + '\n')
                            continue
                    else:
                        user, sep, pw = line.partition(";")
                        pw = strip_text(pw)
                        if len(pw) <= high and len(pw) >= low and sep == ';':
                            if valid_email(pw):
                                semicolonCount += 1
                                continue
                            else:
                                if wrapped_pw(pw):
                                    strip_text(pw, '"')
                                outputCount += 1
                                outfile.write(pw + '\n')
                                continue
                        else:
                            user, sep, pw = line.partition("\t")
                            pw = strip_text(pw, '\t')
                            if len(pw) <= high and len(pw) >= low and sep == '\t':
                                if valid_email(pw):
                                    tabCount += 1
                                    continue
                                else:
                                    if wrapped_pw(pw):
                                        strip_text(pw, '"')
                                    outputCount += 1
                                    outfile.write(pw + '\n')
                                    continue
                            else:
                                elseCount += 1
                                continue
        except ValueError:
            continue


outfile.close()


print('\nColon errors ' + str(colonCount) + ''                                 
      '\nSpace errors ' + str(spaceCount) + ''
      '\nSemi-colon errors ' + str(semicolonCount) + ''
      '\nTab errors ' + str(tabCount) + ''
      '\nMisc bad data ' + str(elseCount) + ''
      '\nNew file has ' + str(outputCount) + ' lines'
      '\nTotal seconds running: ' + str(int(time.time() - startTime)))
