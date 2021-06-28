from ch07.myclass.converter import ScaleConverter
# 단위 변환 클래스 확장
# 온도 변환 - 화씨온도(F) = 섭씨온도(C) X 1.8 + 32

class converters(ScaleConverter):
    def __init__(self,units_from, units_to, facter, offset):
        super().__init__(units_from, units_to, facter)
        self.offset =offset

    def convert(self,val):
        return self.factor * val + self.offset

con = converters("C","F", 1.8, 32)
print("Converting 23C")
print(str(con.convert(23)) + con.units_to)
