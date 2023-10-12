# Compute the area of triangle

a = float(input('Enter A side of triangle: '))
b = float(input('Enter B side of trianlge: '))
c = float(input('Enter C side of triangle: '))

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)