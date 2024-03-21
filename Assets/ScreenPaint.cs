using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScreenPaint : MonoBehaviour
{
    [SerializeField] private Camera cam;
    [SerializeField] private GameObject circle;
    [SerializeField] private int pixelPathToDraw;
    private Vector3 startPos;
    private Vector3 currentPos;

    void Update()
    {
        if(Input.GetMouseButtonDown(0))
        {
            startPos = cam.ScreenToWorldPoint(Input.mousePosition);
        }
        if(Input.GetMouseButton(0))
        {
            currentPos = cam.ScreenToWorldPoint(Input.mousePosition);
        }
        if((currentPos - startPos).magnitude > pixelPathToDraw)
        {
            GameObject obj = Instantiate(circle);
            Vector3 pos = cam.ScreenToWorldPoint(Input.mousePosition);
            obj.transform.position = new Vector3(pos.x, pos.y, -5f);
        }
    }
}

/*когда мышь зажата и двигается
появляются объект круг
на координатах мыши
с частотой 1 круг на 5 пикселей
*/
