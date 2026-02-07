s = input()

mapping = {
    "A":"A",
    "E":"3",
    "H":"H",
    "I":"I",
    "J":"L",
    "L":"J",
    "M":"M",
    "O":"O",
    "S":"2",
    "T":"T",
    "U":"U",
    "V":"V",
    "W":"W",
    "X":"X",
    "Y":"Y",
    "Z":"5",
    "1":"1",
    "2":"S",
    "3":"E",
    "5":"Z",
    "8":"8",
    "0":"0"
}

output = ""
for i in range(len(s)):
    if s[i] in mapping.keys():
        output += mapping[s[i]]
    else:
        output = "ELDDUM"
        break

print(output[::-1])