#Providing Input as well for Future Reference
input =[
997,1582,1790,1798,1094,1831,1879,1730,1995,1702,1680,1869,1964,1777,1862,1928,1997,1741,1604,1691,1219,1458,1749,1717,1786,1665,1724,1998,1589,1828,1953,1848,1500,1590,1968,1948,1323,1800,1986,679,1907,1916,1820,1661,1479,1808,1824,1825,1952,1666,1541,1791,1906,1638,1557,1999,1710,1549,1912,1974,1628,1748,1411,1978,1865,1932,1839,1892,1981,1807,357,912,1443,1972,1816,1890,1029,1175,1522,1750,2001,1655,1955,1949,1660,233,1891,1994,1934,1908,1573,1712,1622,1770,1574,1778,1851,2004,1818,1200,1229,1110,1005,1716,1765,1835,1773,15,1914,1833,1689,1843,1718,1872,390,1941,1178,1670,1899,1864,1913,2010,1855,1797,1767,1673,1657,1607,1305,1341,1662,1845,1980,1534,1789,1876,1849,1926,1958,977,1709,1647,1832,1785,1854,1667,1679,1970,1186,2000,1681,1684,1614,1988,1561,1594,1636,1327,1696,1915,1045,1829,1079,1295,1213,1714,1992,1984,1951,1687,1842,1792,87,1732,428,1799,1850,1962,1629,1965,1142,1040,131,1844,1454,1779,1369,1960,1887,1725,1893,1465,1676,1826,1462,1408,1937,1643,1069,1759
]
total_number = 2020

# TO FIND TWO NUMBERS THAT SUM UP TO 2020
for i, item in enumerate(input):
    for j in range(i+1, len(input)):
        total_of_two_items = input[i] + input[j]
        if(total_of_two_items == total_number):
            print ('{first_item} {second_item}'.format(first_item=input[i], second_item=input[j]))
            print(input[i] * input[j])
            print ('\n')

#TO FIND THREE NUMBERS THAT SUM UP TO 2020
for i, item in enumerate(input):
    for j in range(i+1, len(input)):
        for k in range(j+1, len(input)):
            total_of_three_items = input[i] + input[j] + input[k]
            if(total_of_three_items == total_number):
                print ('{first_item} {second_item} {third_item}'.format(first_item=input[i], second_item=input[j], third_item = input[k]))
                print(input[i]*input[j]*input[k])
                print ('\n')
