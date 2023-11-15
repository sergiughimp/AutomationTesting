
# 'language' method is polimorphic. returns differect things depending on the object. But the name is the same
class Romania:
    def language(self):
        return "romanian"

class France:
    def language(self):
        return "francais"

instance_ro = Romania()
instance_fr = France()

instance_fr.language()
instance_ro.language()
