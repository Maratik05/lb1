import java.util.Scanner;

class MyProgram{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int i = 1;
        while (i*i < a) {
            System.out.println(Math.pow(i, 2));
            i++;

            }
    }
}