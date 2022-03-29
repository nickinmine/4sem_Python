def main(arg):
    arg = arg.replace(' ', '').replace('\n', '')
    arg = arg[arg.find('<section>')+9:arg.find('</section>')]
    arg = arg.replace(';.end,.beginvar', '\0')
    arg = arg.replace('.beginvar', '').replace(';.end,', '')
    arg = arg.replace('"', '').replace(']', '')
    param1 = arg.split('\0')
    for i in range(len(param1)):
        param1[i] = param1[i].strip()
    param2 = []
    for i in param1:
        param2.append(i.split('['))
        #param2[len(param2)-1][0] = param2[len(param2)-1][0][0:].strip()
        param2[len(param2)-1][1] = param2[len(param2)-1][1].split(';')
    res = {}
    for s in param2:
        res[s[0]] = s[1]
    return res


if __name__ == "__main__":
    print(main('<section> .begin var "inorso" [ora_848;dibe_131 ];.end, .begin var\n"isgela"[ orreus_974 ; rige ;ataen_512 ;eran ];.end, .begin var\n"tibeve_820"[orxema ; anor_495 ]; .end,</section>'))
    print(main('<section>.begin var "belece_775" [ anve ; atre_268 ;laa_129 ; anbe];\n.end, .begin var "qumaer"[ atarte ; usrion_138 ; leed; orge ];\n.end,.begin var "onle" [ xeardi_266 ; zaveza ; dianis_330 ]; .end,\n</section>'))
    print(main('<section>.begin var "mais" [ dixein_577; isisbi_456 ; bedi ; edus_9];\n.end, .begin var "isriso_836" [ laat ; usedor ; onar]; .end, .begin\nvar "raxe_832"[ islege_265 ; usbe_490]; .end, .begin var "atge_380" [\nongele ; eserus_69 ; onrate_619 ]; .end,</section>'))
    print(main('<section>.begin var "tesora_738" [ tius; vedi; enes ;socege_395 ];\n.end,.begin var "arma_658" [ estete ; erat; erge_438];.end, </section>'))
    print(main('<section>.begin var"lalaar_468"[oren; enes; ordive_574 ; erve ];\n.end, .begin var "aron"[ legeed_234 ; geisso_826]; .end, .begin\nvar"tier"[ cequ ;erteis; iseddi; reen_478 ]; .end, .begin var\n"onis_739" [ teatus_605 ;beve ]; .end, </section>'))
