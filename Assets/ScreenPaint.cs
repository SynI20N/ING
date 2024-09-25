using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScreenPaint : MonoBehaviour
{
    [SerializeField] private Camera _cam;
    [SerializeField] private GameObject _circle;
    [SerializeField] private float _distanceToDraw;
    private Vector3 _startPos;
    private Vector3 _currentPos;
    private List<GameObject> _spawnedCircles = new List<GameObject>();

    void Update()
    {
        if(Input.GetMouseButtonDown(0))
        {
            _startPos = _cam.ScreenToWorldPoint(Input.mousePosition);
        }
        if(Input.GetMouseButton(0))
        {
            _currentPos = _cam.ScreenToWorldPoint(Input.mousePosition);
        }
        if((_currentPos - _startPos).magnitude > _distanceToDraw)
        {
            Vector3 direction = _currentPos - _startPos;
            int step = 30;
            for(int i = 0; i < step; i++)
            {
                Vector3 dir = _startPos + direction * i / step;
                GameObject obj = Instantiate(_circle);
                _spawnedCircles.Add(obj);
                obj.transform.position = new Vector3(dir.x, dir.y, -5f);
            }
            _startPos = _currentPos;//я забыл эту строчку
        }
    }

    public void ClearScreen()
    {
        foreach(GameObject circle in _spawnedCircles)
        {
            Destroy(circle);
        }
        _spawnedCircles.Clear();
    }
}

/*когда мышь зажата и двигается
появляются объект круг
на координатах мыши
с частотой 1 круг на 5 пикселей
*/

// получились лучи на экране. можно исследовать почему?
// if((_currentPos - _startPos).magnitude > _distanceToDraw)
// {
//     Vector3 direction = _currentPos - _startPos;
//     int step = 100;
//     for(int i = 0; i < step; i++)
//     {
//         direction = _startPos + direction * i / step;
//         GameObject obj = Instantiate(_circle);
//         obj.transform.position = new Vector3(direction.x, direction.y, -5f);
//     }
//     _startPos = _currentPos;//я забыл эту строчку
// }
