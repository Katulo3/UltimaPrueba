from cuentas.forms import CreateUserForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView, UpdateView

# Mostrar clientísimos
# class ListClientes(ListView):
#     model = Cliente
#     template_name = "clientes/clientes.html"
#     fields = "__all__"

#     def listar_clientes(self, **kwargs):
#         # Hereda  y extiende el contexto de la clase
#         contexto = super().get_context_data(**kwargs)

#         clientes = Cliente.objects.all()
#         contexto["clientes"] = clientes
#         return contexto

#     # Ordena en un query los clientes por orden alfabético del nombre
#     def get_queryset(self):
#         orden = super().get_queryset().order_by("nombre")
#         return orden


# class CrearCliente(CreateView):
#     model = Cliente
#     template_name = "clientes/crud_clientes.html"
#     success_url = reverse_lazy("clientes")
#     fields = "__all__"


# class EditarCliente(UpdateView):
#     model = Cliente
#     template_name = "clientes/crud_clientes.html"
#     success_url = reverse_lazy("clientes")
#     fields = "__all__"


# # class EliminarCliente(DeleteView):
# #     model = Cliente
# #     template_name = "clientes/crud_cliente.html"
# #     success_url = reverse_lazy("list_clientes")


class VerUsuarios(ListView):
    model = User
    template_name = "cuentas/usuarios.html"

    def listar_usuarios(self, **kwargs):
        # Hereda  y extiende el contexto de la clase
        contexto = super().get_context_data(**kwargs)

        usuarios = User.objects.all()
        contexto["usuarios"] = usuarios
        return contexto


def registrar_usuarios(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cuentas:usuarios")
    contexto = {"form": form}
    return render(request, "cuentas/registrar.html", contexto)
