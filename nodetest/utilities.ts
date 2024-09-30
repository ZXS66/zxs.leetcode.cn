import { ListNode } from "./models";

/** generate `ListNode` from array of number */
export function genListNode(array: number[]): ListNode | null {
    const head = new ListNode(0);
    let cur = head;
    for (let i = 0; i < array.length; i++) {
        cur.next = new ListNode(array[i]);
        cur = cur.next;
    }
    return head.next;
}
/** format the `ListNode` as printable string */
export function fmtListNode(headNode: ListNode | null) {
    if (!headNode) {
        return '[]';
    }
    const values = new Array();
    let cur: ListNode | null = headNode;
    while (cur) {
        values.push(cur.val);
        cur = cur.next;
    }
    return "[" + values.join(',') + "]";
}
