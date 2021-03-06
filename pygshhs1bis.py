#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Filename          : pygshhs1bis.py
#  Created by        : StephPen - stephpen@gmail.com
#  Update            : 11:14 02/01/2011
#
#  (c) 2008 by Stephane PENOT
#      See COPYING file for copying and redistribution conditions.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#  Comments          :
#
#
#
#
#
#  Contact: <stephpen@gmail.com>
#




from Polygon import *
import os.path
import sys



#path = '/home/spenot/gshhs/'
path = './'
path_BD = path + 'bd/'

if len(sys.argv) < 2 :
    print "Use pygshhs.py [c, l, i, h, f] !"
    print "By default it's resolution c"
    level = 'c'
else :
    level = sys.argv[1]

path_BD_f = path_BD + 'bd_' + level
if os.path.isdir(path_BD_f) == 0 :
    os.mkdir(path_BD_f)

pas1 = 45

i=1
while i<=5 :
    x=0
    while x<360 :
        y=-90
        while y<90 :
            path_poly_dir = path_BD + str(x) + '_' + str(y) + '_to_' + str(x + pas1) + '_' + str(y + pas1)

            path_poly_1 = path_poly_dir +'/' + level + str(i) + '.dat'
            poly_start_1 = Polygon(path_poly_1)

            path_poly_f_dir = path_BD_f +'/'+ str(x) + '_' + str(y) + '_to_' + str(x + pas1) + '_' + str(y + pas1)
            if os.path.isdir(path_poly_f_dir) == 0 :
                os.mkdir(path_poly_f_dir)


            path_poly_f = path_poly_f_dir+ '/' + level + str(i) + '.dat'
            print path_poly_f
            poly_start_1.write(path_poly_f)

            y=y+pas1

        x=x+pas1

    i=i+1

# On vide la memoire
poly_start_1 = 0



