/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
};
*/

class Solution {
    public Node construct(int[][] grid) {
        //leaf node: has the same value and isLeaf = true, val = grid value, no children
        // non-leaf node: different values, isLeaf = false, val is any value.
        // recurse for each of the children
        int nrow = grid.length;
        int ncol = grid[0].length;
        return constructNode(grid, new int[]{0, 0}, new int[]{0, ncol - 1}, new int[]{nrow - 1, 0}, new int[]{nrow - 1, ncol - 1});
        
    }
    public Node constructNode(int[][] grid, int[] topLeftPoint, int[] topRightPoint, int[] bottomLeftPoint, int[] bottomRightPoint) {
        int midCol = (topLeftPoint[1] + topRightPoint[1]) / 2;
        int midRow = (topLeftPoint[0] + bottomLeftPoint[0]) / 2;
        //System.out.printf("%d %d %d %d\n", midCol ,topRightPoint[1] , midRow , bottomLeftPoint[0]);
        if (midCol == topRightPoint[1] && midRow == bottomLeftPoint[0])
            return new Node(grid[midRow][midCol] == 1, true);
        
        // topLeftBlock
        Node topLeft = constructNode(grid, topLeftPoint, new int[]{topRightPoint[0], midCol}, new int[]{midRow, bottomLeftPoint[1]}, new int[] {midRow, midCol});
        //topRightBlock
        Node topRight = constructNode(grid, new int[]{topLeftPoint[0], midCol + 1}, topRightPoint, new int[]{midRow, midCol + 1}, new int[]{midRow, bottomRightPoint[1]});
        
        //bottomLeftBlock
        Node bottomLeft = constructNode(grid, new int[]{midRow + 1, topLeftPoint[1]}, new int[]{midRow + 1, midCol}, bottomLeftPoint, new int[]{bottomRightPoint[0], midCol});
        //bottomRightBlock
        Node bottomRight = constructNode(grid, new int[]{midRow + 1, midCol + 1}, new int[]{midRow + 1, topRightPoint[1]}, new int[]{bottomLeftPoint[0], midCol + 1}, bottomRightPoint);
        

        boolean isTotalLeaf = topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf;
        if (isTotalLeaf) {
            boolean isTotalTrue = topLeft.val && topRight.val && bottomLeft.val && bottomRight.val;
            if (isTotalTrue)
                return new Node(true, true);
            boolean isTotalFalse = topLeft.val || topRight.val || bottomLeft.val || bottomRight.val;
            if (!isTotalFalse)
                return new Node(false, true);
        }
        
        return new Node(true , false, topLeft, topRight, bottomLeft, bottomRight);
        
    } 
}