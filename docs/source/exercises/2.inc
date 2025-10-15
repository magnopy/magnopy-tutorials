.. admonition:: Exercises

    1.  Create an instance of :external:py:class:`magnopy.Convention` for the following 
        Hamiltonians

        .. math::
        
            \mathcal{H}_1 = - \sum_{i \neq j} J_{ij} \mathbf{S}_i \cdot \mathbf{S}_j
            \\
            \mathcal{H}_2 = - \sum_{i, j} J_{ij} \mathbf{S}_i \cdot \mathbf{S}_j
            \\
            \mathcal{H}_3 = 0.5 \sum_{i, j} J_{ij} \mathbf{S}_i \cdot \mathbf{S}_j
            \\
            \mathcal{H}_4 = - \sum_{i < j} J_{ij} \mathbf{e}_i \cdot \mathbf{e}_j