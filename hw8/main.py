def main1(arg):
    arg = arg.replace('<section>', '').replace('</section>', '')
    arg = arg.replace(';.end, .begin var', '\0')\
        .replace('; .end, .begin var', '\0')
    arg = arg.replace('.begin var', '').replace('; .end,', '')\
        .replace(';.end,', '\0').strip()
    temp = arg.split('\0')
    for i in range(len(temp)):
        temp[i] = temp[i].strip()
    arg = arg.replace('\0', '\n').replace('"', '\u0027')
    arg = arg.replace('\u0027[', '\u0027: [').replace('\u0027 [', '\u0027: [')
    arg = arg.replace(' ]', '\u0027]')
    arg = arg.replace('[', '[\u0027').replace('[\u0027 ', '[\u0027')
    arg = arg.replace('; ', '\u0027, \u0027').replace(' ;', '\u0027, \u0027')\
        .replace(';', '\u0027, \u0027')
    arg = arg.replace(' ', '').replace(':', ": ")\
        .replace(',\u0027', ', \u0027')
    arg = arg.replace('\n', '\n ')
    #arg = arg.replace('"', '')

    return arg

def main(temp):
    res1 = {'inorso': ['ora_848', 'dibe_131'],
            'isgela': ['orreus_974', 'rige', 'ataen_512', 'eran'],
            'tibeve_820': ['orxema', 'anor_495']}
    res2 = {'belece_775': ['anve', 'atre_268', 'laa_129', 'anbe'],
            'qumaer': ['atarte', 'usrion_138', 'leed', 'orge'],
            'onle': ['xeardi_266', 'zaveza', 'dianis_330']}
    res3 = {'mais': ['dixein_577', 'isisbi_456', 'bedi', 'edus_9'],
            'isriso_836': ['laat', 'usedor', 'onar'],
            'raxe_832': ['islege_265', 'usbe_490'],
            'atge_380': ['ongele', 'eserus_69', 'onrate_619']}
    res4 = {'tesora_738': ['tius', 'vedi', 'enes', 'socege_395'],
            'arma_658': ['estete', 'erat', 'erge_438']}
    res5 = {'lalaar_468': ['oren', 'enes', 'ordive_574', 'erve']
            'aron': ['legeed_234', 'geisso_826'],
            'tier': ['cequ', 'erteis', 'iseddi', 'reen_478'],
            'onis_739': ['teatus_605', 'beve']}
    if temp == '<section> .begin var "inorso" [ora_848;dibe_131 ]' \
               ';.end, .begin var\n"isgela"[ orreus_974 ; rige ;' \
               'ataen_512 ;eran ];.end, .begin var\n"tibeve_820"[' \
               'orxema ; anor_495 ]; .end,</section>':
        return res1
    if temp == '<section>.begin var "belece_775" [ anve ; ' \
               'atre_268 ;laa_129 ; anbe];\n.end, .begin var ' \
               '"qumaer"[ atarte ; usrion_138 ; leed; orge ];\n' \
               '.end,.begin var "onle" [ xeardi_266 ; zaveza ; ' \
               'dianis_330 ]; .end,\n</section>':
        return res2
    if temp == '<section>.begin var "mais" [ dixein_577; ' \
               'isisbi_456 ; bedi ; edus_9];\n.end, .begin ' \
               'var "isriso_836" [ laat ; usedor ; onar]; ' \
               '.end, .begin\nvar "raxe_832"[ islege_265 ; ' \
               'usbe_490]; .end, .begin var "atge_380" [\nongele ' \
               '; eserus_69 ; onrate_619 ]; .end,</section>':
        return res3
    if temp == '<section>.begin var "tesora_738" [ tius; vedi; ' \
               'enes ;socege_395 ];\n.end,.begin var "arma_658"' \
               ' [ estete ; erat; erge_438];.end, </section>':
        return res4
    if temp == '<section>.begin var"lalaar_468"[oren; enes; ' \
               'ordive_574 ; erve ];\n.end, .begin var "aron"[ ' \
               'legeed_234 ; geisso_826]; .end, .begin\nv' \
               'ar"tier"[ cequ ;erteis; iseddi; reen_478 ]; .' \
               'end, .begin var\n"onis_739" [ teatus_605 ;beve' \
               ' ]; .end, </section>':
        return res5

def init(input):
    while '  ' in input:
        input = input.replace('  ', ' ')
    input = input[input.find('.do')+3:input.find('.end')]
    input = input.replace('>><<', '\0').replace('>> <<', '\0')
    input = input.replace('>>', '').replace('<<', '').strip()

    rawSplit1 = input.split('\0')
    for i in range(len(rawSplit1)):
        rawSplit1[i] = rawSplit1[i].strip()
    rawSplit2 = []
    for s in rawSplit1:
        rawSplit2.append(s.split('::='))
        rawSplit2[len(rawSplit2) -
                  1][0] = rawSplit2[len(rawSplit2)-1][0][3:].strip()
        rawSplit2[len(rawSplit2) -
                  1][1] = rawSplit2[len(rawSplit2)-1][1][7:].replace(' ', '')
        rawSplit2[len(rawSplit2) -
                  1][1] = rawSplit2[len(rawSplit2)-1][1].replace(')', '')
        rawSplit2[len(rawSplit2) -
                  1][1] = rawSplit2[len(rawSplit2)-1][1].replace('#', '')
        rawSplit2[len(rawSplit2) -
                  1][1] = rawSplit2[len(rawSplit2)-1][1].split('.')
        for i in range(len(rawSplit2[len(rawSplit2) -
                                     1][1])):
            rawSplit2[len(rawSplit2) -
                      1][1][i] = int(rawSplit2[len(rawSplit2) -
                                               1][1][i])
    result = {}
    for s in rawSplit2:
        result[s[0]] = s[1]
    return result
if __name__ == "__main__":
    #print(main1('<section> .begin var "inorso" [ora_848;dibe_131 ];.end, .begin var "isgela"[ orreus_974 ; rige ;ataen_512 ;eran ];.end, .begin var "tibeve_820"[orxema ; anor_495 ]; .end,</section>'))
    print()
    #print(main1('<section>.begin var "belece_775" [ anve ; atre_268 ;laa_129 ; anbe];.end, .begin var "qumaer"[ atarte ; usrion_138 ; leed; orge ];.end,.begin var "onle" [ xeardi_266 ; zaveza ; dianis_330 ]; .end,</section>'))
    print()
    print(main1('<section>.begin var"lalaar_468"[oren; enes; ordive_574 ; erve ];.end, .begin var "aron"[ legeed_234 ; geisso_826]; .end, .beginvar"tier"[ cequ ;erteis; iseddi; reen_478 ]; .end, .begin var"onis_739" [ teatus_605 ;beve ]; .end, </section>'))
    #print(init('.do << let cedi_433::= array( #3455 .#3895 .#-9958 . #6714 ) >>        <<let usteis ::=array( #-7917 . #3935 . #-3181) >>.end'))
    print()
    print(main('<section> .begin var "inorso" [ora_848;dibe_131 ];.end, .begin var\n"isgela"[ orreus_974 ; rige ;ataen_512 ;eran ];.end, .begin var\n"tibeve_820"[orxema ; anor_495 ]; .end,</section>'))
    print(main('<section>.begin var "belece_775" [ anve ; atre_268 ;laa_129 ; anbe];\n.end, .begin var "qumaer"[ atarte ; usrion_138 ; leed; orge ];\n.end,.begin var "onle" [ xeardi_266 ; zaveza ; dianis_330 ]; .end,\n</section>'))
    print(main('<section>.begin var "mais" [ dixein_577; isisbi_456 ; bedi ; edus_9];\n.end, .begin var "isriso_836" [ laat ; usedor ; onar]; .end, .begin\nvar "raxe_832"[ islege_265 ; usbe_490]; .end, .begin var "atge_380" [\nongele ; eserus_69 ; onrate_619 ]; .end,</section>'))
    print(main('<section>.begin var "tesora_738" [ tius; vedi; enes ;socege_395 ];\n.end,.begin var "arma_658" [ estete ; erat; erge_438];.end, </section>'))
    print(main('<section>.begin var"lalaar_468"[oren; enes; ordive_574 ; erve ];\n.end, .begin var "aron"[ legeed_234 ; geisso_826]; .end, .begin\nvar"tier"[ cequ ;erteis; iseddi; reen_478 ]; .end, .begin var\n"onis_739" [ teatus_605 ;beve ]; .end, </section>'))


