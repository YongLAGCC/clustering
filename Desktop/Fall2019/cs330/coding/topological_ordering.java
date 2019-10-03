
import java.io.File;
import java.util.*;
import java.io.BufferedWriter;
import java.io.FileWriter;

import java.io.File;

class topological_ordering {

    public static void main(String[] args) throws Exception {

        File file = new File("input");
        Scanner sc = new Scanner(file);
        int totalRow = Integer.valueOf(sc.nextLine());

        String line = "";

        LinkedList<Integer>[] layer;
        layer = new LinkedList[totalRow];

        for (int row = 0; row < totalRow; row++) {

            layer[row] = new LinkedList<>();
            char[] chars = sc.nextLine().toCharArray();
            line = new String(chars);

            String ab [] = new String [totalRow];
            ab = line.split(",");

            for (int i = 0; i < ab.length; i++) {
                if ( !( ab[i].equals("-") ) ) {
                    layer[row].addLast( Integer.parseInt(ab[i]) );
                } else
                    continue;
            }
        }

        int list [] = new int[totalRow];
        for (int i = 0; i < totalRow; i ++){
            for(int c: layer[i]){

                if( c != '-')
                    list[c] +=1;
                else
                    continue;
            }
        }

        LinkedList<Integer> topOrder = new LinkedList<>();  // w
        LinkedList<Integer> middleWareForSaveZero = new LinkedList<>();

        for( int i = 0; i<totalRow; i++) {
            if (list[i] == 0) {
                middleWareForSaveZero.addLast(i);
            }
        }

            while (!middleWareForSaveZero.isEmpty() ) {
                int node = middleWareForSaveZero.pollFirst();
                topOrder.addLast(node);
                for( int i : layer[node]) {
                    list[i] --;
                    if(list[i] ==0) {
                        middleWareForSaveZero.addLast(i);
                    }
            }
            }


            BufferedWriter writer = new BufferedWriter(new FileWriter("output"));
            for(int n: topOrder){
                writer.write(n+"");
                writer.write("\n");
            }
                
                writer.close();
    }

}


