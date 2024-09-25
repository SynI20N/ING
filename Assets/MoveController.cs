using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveController : MonoBehaviour
{
    [SerializeField] private float _speed = 1;

    void Update()
    {
        Vector3 direction = new Vector3(0,0,0);
        if(Input.GetKey("d"))
        {
            direction = new Vector3(1, 0, 0);
        }
        if(Input.GetKey("a"))
        {
            direction = new Vector3(-1, 0, 0);
        }
        if(Input.GetKey("w"))
        {
            direction = new Vector3(0, 1, 0);
        }
        if(Input.GetKey("s"))
        {
            direction = new Vector3(0, -1, 0);
        }
        if(Input.anyKey)
        {
            Vector3 moveVector = _speed * Time.deltaTime * direction;
            transform.position += moveVector;
        }
    }
}
