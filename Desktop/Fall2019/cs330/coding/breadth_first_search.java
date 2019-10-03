import java.util.*;
import java.io.File;
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;

class breadth_first_search {

    public static void main(String[] args) throws Exception {
        LinkedList<Integer>[] nodes;
        LinkedList<Integer>[] outputGraph;

        File file = new File("input");
        Scanner sc = new Scanner(file);
        int totalRow = Integer.valueOf(sc.nextLine());
        int startnode = Integer.valueOf(sc.nextLine());

        String[] line1 = new String[totalRow];
        String line = "";

        nodes = new LinkedList[totalRow];
        outputGraph = new LinkedList[totalRow];

        for (int i = 0; i < totalRow; i++) {
            nodes[i] = new LinkedList<>();
            outputGraph[i] = new LinkedList<>();
        }

        for (int row = 0; row < totalRow; row++) {
            char[] chars = sc.nextLine().toCharArray();
            line = new String(chars);
            line1[row] = line;
            String[] r = line1[row].split(",");
            for (int i = 0; i < r.length; i++)
                nodes[row].add(Integer.parseInt(r[i]));
//            System.out.println(line1[row]);
        }
        boolean visited[] = new boolean[totalRow];

        for (int i = 0; i < totalRow; i++) {
            visited[i] = false;
        }
        visited[startnode] = true;

        LinkedList<Integer>[] layer;
        layer = new LinkedList[totalRow];
        layer[0] = new LinkedList<>();

        layer[0].add(startnode);

        int i = 0; // layer count to be 1.
        //outputGraph = ;

        while (layer[i].size() != 0) {
            layer[i + 1] = new LinkedList<>();

            for (int n : layer[i]) {

                for (int j : nodes[n]) {
                    if (visited[j] != true) {
                        visited[j] = true;
                        layer[i + 1].addLast(j);
                        outputGraph[n].add(j);
                        outputGraph[j].add(n);
                    }
                }
            }
            i++;
        }
        BufferedWriter writer = new BufferedWriter(new FileWriter("output"));
            for (int h = 0; h < outputGraph.length; h++) {
                for (int m : outputGraph[h]) {
                    writer.write(m + ",");
                }
                writer.write("\n");
            }
        writer.close();




        }
    }
