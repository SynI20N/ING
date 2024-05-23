using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ColoringMat : MonoBehaviour
{
    [SerializeField] private Material _mat;
    [SerializeField] private List<Color> _colors;

    public void ColorMaterial(int index)
    {
        if (index < 0 || index >= _colors.Count)
        {
            return;
        }
        _mat.SetColor("_Color", _colors[index]);
    }
}
