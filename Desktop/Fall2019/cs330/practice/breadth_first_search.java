import java.io.File; 
import java.io.FileNotFoundException;
import java.nio.channels.WritePendingException;
//import com.sun.org.apache.xpath.internal.SourceTree;
//import javafx.scene.effect.Light.Spot; 
import java.util.*; 
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class breadth_first_search{
//public static int totalRow; 


        public static void main(String[] args) throws Exception 
        { 
          
        LinkedList<Integer> [] nodes;
        LinkedList<Integer> [] outputGraph;

        
        File file = new File("input");
        Scanner sc = new Scanner(file);
        int totalRow = Integer.valueOf(sc.nextLine() );
        int startnode = Integer.valueOf(sc.nextLine());
         
        String [] line1 = new String [totalRow];
        String line = ""; 

      
        for (int i = 0; i < totalRow; i ++){
        	nodes[i] = new LinkedList<>();
        	outputGraph[i] = new LinkedList<>();
        }
        
         

        for (int row = 0; row < totalRow; row++) {
            char[] chars = sc.nextLine().toCharArray();
            line = new String(chars);
            line1[row] = line ; 
            String [] r = line1[row].split(",");
            for(int i = 0; i < r.length; i++ )
              nodes[row].add( Integer.parseInt(r[i]) ); 
            //System.out.println( line1[row] );
            
            }
        boolean visited [] = new boolean [totalRow];
        
        for( int i = 0; i< totalRow; i ++){
          visited[i] = false; 
        }
        visited[0] = true; 
        
        LinkedList<Integer> [] layer;
        layer[0] = new LinkedList<>();
        
        
        
        layer[0].add(startnode);
        
        int i = 0; // layer count to be 1.
        //outputGraph = ; 

        while(layer[i].size() != 0){
          layer[i+1] = new LinkedList<>();
          for (int j = 0; j < layer[i].size(); j ++ ){
            for( int n: nodes[j]){
              layer[i+1].addLast(n);
              if(visited[n] != true){
                visited[n] = true; 
                outputGraph[i].add(n);
                outputGraph[i].add(layer[i].getFirst());

                layer[i+1].add(n);
              }
            }
          }
          i++;
        }


        // boolean visited [] = new boolean[totalRow];
          
        
        // for(int i = 0; i < totalRow; i ++){
        //   System.out.print(val[i] + "  !!");
        
        // }



            

          }
        }